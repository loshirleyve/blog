class ImageCompress {
  async compress (file, config = {}) {
    if (!(file instanceof Blob)) {
      throw new Error('compress(): First arg must be a Blob object or a File object.')
    }
    if (typeof config !== 'object') {
      config = Object.assign({
        quality: config
      })
    }

    config.quality = Number(config.quality)
    if (Number.isNaN(config.quality)) {
      return file
    }
    const dataURL = await this.filetoDataURL(file)
    let originalMime = dataURL.split(',')[0].match(/:(.*?);/)[1] // 原始图像图片类型
    let mime = 'image/jpeg' // 默认压缩类型
    if (this.checkImageType(config.type)) {
      mime = config.type
      originalMime = config.type
    }
    const image = await this.dataURLtoImage(dataURL)
    const canvas = await this.imagetoCanvas(image, Object.assign({}, config))
    const compressDataURL = await this.canvastoDataURL(canvas, config.quality, mime)
    const compressFile = await this.dataURLtoFile(compressDataURL, originalMime)
    return {
      base64: compressDataURL,
      file: compressFile
    }
  }

  /**
   * 将File（Blob）对象转变为一个dataURL(base64)字符串
   * @returns {Promise}
   */
  filetoDataURL (file) {
    return new Promise((resolve) => {
      const reader = new FileReader()
      reader.onloadend = e => resolve(e.target.result)
      reader.readAsDataURL(file)
    })
  }

  /**
   * 将dataURL字符串转变为image对象
   * @param dataURL
   * @returns {Promise}
   */
  dataURLtoImage (dataURL) {
    return new Promise((resolve, reject) => {
      const img = new Image()
      img.onload = () => resolve(img)
      img.onerror = () => reject(new Error('dataURLtoImage(): dataURL is illegal'))
      img.src = dataURL
    })
  }

  /**
   * 将一个image对象转变为一个canvas对象
   * @param image
   * @param config
   * @returns {Promise<HTMLCanvasElement>}
   */
  async imagetoCanvas (image, config = {}) {
    const cvs = document.createElement('canvas')
    const ctx = cvs.getContext('2d')
    let height = image.height
    let width = image.width
    console.log('原图宽，，高，，', width, height)

    // 设置宽高
    for (const i in config) {
      if (Object.prototype.hasOwnProperty.call(config, i)) {
        config[i] = Number(config[i])
      }
    }

    if (!config.scale) {
      width = config.width || config.height * image.width / image.height || image.width
      height = config.height || config.width * image.height / image.width || image.height
    } else {
      // 缩放比例0-10，不在此范围则保持原来图像大小
      const scale = config.scale > 0 && config.scale < 10 ? config.scale : 1
      width = image.width * scale
      height = image.height * scale
    }

    const maxW = 2000
    const maxH = 2000
    if (width < height && height > maxH) {
      width = parseInt(maxH * width / height)
      height = maxH
    } else if (width >= height && width > maxW) {
      height = parseInt(maxW * height / width)
      width = maxW
    }
    console.log('canvas width, height: ---->>>', width, height)

    // 设置canvas的高宽
    cvs.height = height
    cvs.width = width

    ctx.drawImage(image, 0, 0, cvs.width, cvs.height)
    return cvs
  }

  /**
   * 将一个Canvas对象转变为一个dataURL字符串
   * 该方法可以做压缩处理
   * @param canvas
   * @param quality
   * @param type
   * @returns {Promise<string>}
   */
  async canvastoDataURL (canvas, quality, type) {
    if (!this.checkImageType(type)) {
      type = 'image/jpeg'
    }
    return canvas.toDataURL(type, quality)
  }

  /**
   * 将一个dataURL字符串转变为一个File（Blob）对象
   * 转变时可以确定File对象的类型
   * @param dataURL
   * @param type
   * @returns {Promise<Blob>}
   */
  async dataURLtoFile (dataURL, type) {
    const arr = dataURL.split(',')
    let mime = arr[0].match(/:(.*?);/)[1]
    const bstr = atob(arr[1])
    let n = bstr.length
    const u8arr = new Uint8Array(n)
    while (n--) {
      u8arr[n] = bstr.charCodeAt(n)
    }
    if (this.checkImageType(type)) {
      mime = type
    }
    return new Blob([u8arr], {
      type: mime
    })
  }

  checkImageType (type) {
    return ['image/png', 'image/jpeg', 'image/gif'].some(i => i === type)
  }
}

export default new ImageCompress()
