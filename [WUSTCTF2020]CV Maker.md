# [WUSTCTF2020]CV Maker



![image-20210527162809934]([WUSTCTF2020]CV Maker/image-20210527162809934.png)

## 知识点

- 文件上传`exif_imagetype`绕过

## 解题

![image-20210527163234992]([WUSTCTF2020]CV Maker/image-20210527163234992.png)

上传可以看到有一个`exif_imagetype`函数

我们只需要在我们的一句话马前面加上文件头就可以通过

![image-20210527163322618]([WUSTCTF2020]CV Maker/image-20210527163322618.png)

![image-20210527162717344]([WUSTCTF2020]CV Maker/image-20210527162717344.png)



