# [极客大挑战 2019]BuyFlag

## 考点

- cookie伪造
- strcmp()函数漏洞   https://blog.csdn.net/cherrie007/article/details/77473817

## 解题

![image-20220128161219757]([极客大挑战 2019]BuyFlag/image-20220128161219757.png)

可以看到有一个身份认证，和两个需要post传参的参

![image-20220128161358116]([极客大挑战 2019]BuyFlag/image-20220128161358116.png)

请求包里有一个user=0，可以猜出这个user就是做身份认证的

![image-20220128161459371]([极客大挑战 2019]BuyFlag/image-20220128161459371.png)