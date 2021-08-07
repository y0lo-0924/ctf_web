# [HarekazeCTF2019]Avatar Uploader 1

![image-20210715110540980]([HarekazeCTF2019]Avatar Uploader 1/image-20210715110540980.png)

## 考点：

- `finfo_file()`函数
- `getimagesize()`函数

## 解题

upload源码

https://github.com/TeamHarekaze/HarekazeCTF2019-challenges/blob/master/avatar_uploader_1/server/public/upload.php

```php
<?php
error_reporting(0);

require_once('config.php');
require_once('lib/util.php');
require_once('lib/session.php');

$session = new SecureClientSession(CLIENT_SESSION_ID, SECRET_KEY);

// check whether file is uploaded
if (!file_exists($_FILES['file']['tmp_name']) || !is_uploaded_file($_FILES['file']['tmp_name'])) {
  error('No file was uploaded.');
}

// check file size
if ($_FILES['file']['size'] > 256000) {
  error('Uploaded file is too large.');
}

// check file type
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$type = finfo_file($finfo, $_FILES['file']['tmp_name']);
finfo_close($finfo);
if (!in_array($type, ['image/png'])) {
  error('Uploaded file is not PNG format.');
}

// check file width/height
$size = getimagesize($_FILES['file']['tmp_name']);
if ($size[0] > 256 || $size[1] > 256) {
  error('Uploaded image is too large.');
}
if ($size[2] !== IMAGETYPE_PNG) {
  // I hope this never happens...
  error('What happened...? OK, the flag for part 1 is: <code>' . getenv('FLAG1') . '</code>');
}

// ok
$filename = bin2hex(random_bytes(4)) . '.png';
move_uploaded_file($_FILES['file']['tmp_name'], UPLOAD_DIR . '/' . $filename);

$session->set('avatar', $filename);
flash('info', 'Your avatar has been successfully updated!');
redirect('/');
```

在检查文件类型时，`finfo_file()`函数检测上传图片的类型是否是`image/png`
 在检查文件长宽时，`getimagesize()` 函数用于获取图像大小及相关信息，成功将返回一个数组，但其后面还有：

```php
if ($size[2] !== IMAGETYPE_PNG) {
  // I hope this never happens...
  error('What happened...? OK, the flag for part 1 is: <code>' . getenv('FLAG1') . '</code>');
```

索引`2`不是**PNG**，将输出`part 1`的flag

对于`getimagesize()` 函数返回的数组：

```php
Array
(
    [0] => 290
    [1] => 69
    [2] => 3
    [3] => width="290" height="69"
    [bits] => 8
    [mime] => image/png
)
```

结果解释：

    索引 0 给出的是图像宽度的像素值
    索引 1 给出的是图像高度的像素值
    索引 2 给出的是图像的类型，返回的是数字，其中1 = GIF，2 = JPG，3 = PNG，4 = SWF，5 = PSD，6 = BMP，7 = TIFF(intel byte order)，8 = TIFF(motorola byte order)，9 = JPC，10 = JP2，11 = JPX，12 = JB2，13 = SWC，14 = IFF，15 = WBMP，16 = XBM
    索引 3 给出的是一个宽度和高度的字符串，可以直接用于 HTML 的 <image> 标签
    索引 bits 给出的是图像的每种颜色的位数，二进制格式
    索引 channels 给出的是图像的通道值，RGB 图像默认是 3
    索引 mime 给出的是图像的 MIME 信息，此信息可以用来在 HTTP Content-type 头信息中发送正确的信息，如：header("Content-type: image/jpeg");

为了获取到flag，我们需要绕过函数finfo_file()或函数getimagesize() 的验证
函数finfo_file()其主要是识别PNG文件十六进制下的第一行信息，若保留文件头信息，破坏掉文件长宽等其余信息，也就可以绕过getimagesize() 函数的检验
使用010 Editor将图片其余数据删掉，只保留文件头：

![image-20210715110839357]([HarekazeCTF2019]Avatar Uploader 1/image-20210715110839357.png)

![image-20210715110848005]([HarekazeCTF2019]Avatar Uploader 1/image-20210715110848005.png)