# word2html 说明

## 功能
用于把 .docx 类型的 word 文件转成 html 文件

### package.json
在父级项目的 package.json 里的 `scripts` 加上 `cd word2html && start word2html.exe` 运行命令, 其中 word2html 为项目文件夹名，word2html.exe 为把 word 文件转成 html 文件的可执行命令

## 使用说明
- 把 `.docx` 类型的 word 文档放于 word2html 文件夹下
- 在www 目录下执行 `npm run word2html`，最终生成的 html 会被放置在 word2html/html 文件夹下
- 也可直接双击 word2html.exe 执行

