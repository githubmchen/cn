# 存储空间默认加密

为了存储在 OSS 数据中心的磁盘上时保护数据，您可以对存储空间设置默认加密，从而对其中默认加密生效期间存储的对象进行服务器端加密。这些对象使用京东云的KMS(Key Management System) 托管密钥 (SSE-KMS) 在服务器端进行加密。在使用服务器端加密时，OSS 将对象保存到其数据中心的磁盘上之前对其进行加密，并在下载对象时对其进行解密。只要验证了您的请求并且拥有访问权限，那么您访问加密和未加密对象的方式就没有区别。

默认加密可适用于所有OSS存储空间，若您更改现有存储空间的默认加密设置，不会对已经保存在存储空间的文件产生影响,仅对默认加密设置生效期间的存储数据有效。存储空间的默认加密，为加密整个存储空间的对象提供了便利，目前不支持使用您创建KMS客户主密钥 (Customer Masker Key,CMK) 加密您的文件，仅支持KMS提供的服务秘钥加密。


## OSS静态加密主要应用场景 

OSS通过服务端加密机制，提供静态数据保护。适合于用户对于文件的存储有高安全性或者合规性要求的应用场景。例如，深度学习样本文件的存储。

## 默认加密设置

您可以使用我们兼容 S3 的API ，或者 AWS 开发工具包或者OSS的控制台启用默认加密。其中最简单的方式是使用OSS管理控制台。在您完成存储空间默认加密设置后，默认加密生效期间上传文件的将自动为您创建KMS服务密钥加密您的文件。对 OSS 存储空间使用默认加密不会产生新的费用。使用S3 API 请求配置默认加密功能会产生标准OSS请求费用。具体请求定价请参阅 [OSS计费规则](https://docs.jdcloud.com/cn/object-storage-service/billing-rules)对于 SSE-KMS 加密密钥存储， Key Management Service（KMS） 的费用目前免费。

需要注意的是为存储空间启用默认加密后，将会应用以下加密行为：

 *  在启用默认加密之前，存储空间中已存在的对象的加密没有变化。
 
 *  目前仅支持对存储空间级别的加密，如果您使用 S3 API 中的put object创建Object时，即使请求中携带x-aws-server-side-encryption 的HTTP Header也是无效设置。
 
 *  并且您需要使用兼容S3 API 时，上传下载等操作均仅支持HTTPS协议，这点请您特别注意。
 
同时通过服务器端加密存储的Object，使用以下s3 API请求该加密过的object,OSS会返回x-aws-server-side-encryption头：

PutObject

CopyObject

PostObject

InitiateMultipartUpload

UploadPart

UploadPartCopy

CompleteMultipartUpload

GetObject

HeadObject

##### Meta信息
通过服务器端加密-KMS托管主密钥模式存储的Object，对象的Meta信息会增加以下字段：

|名称|描述|示例|
|:-|:-|:-|
|x-aws-server-side-encryption|指定服务端加密方式|x-aws-server-side-encryption：aws:kms|

##  使用OSS管理控制台，设置默认加密

1.登入控制台->对象存储->空间管理->进入某个Bucket->空间设置->默认加密

![存储空间默认加密](../../../../../image/Object-Storage-Service/OSS-96.png)

2.点击修改，设置该存储空间的默认加密方式。

![存储空间默认加密](../../../../../image/Object-Storage-Service/OSS-95.png)

细节说明：

   - 若您不设置存储空间默认加密方式则所有的已有或者新建的存储空间都没有开启默认加密，存储空间的默认加密方式仅支持SSE-KMS方式。

   - 设置默认加密只对新增文件生效，已经保存在存储空间中的文件将不会受到加密方式改变的影响。

   - 如果您设置使用 SSE-KMS 的默认加密，请确保使用签名版本 4  对所有 PUT 和 GET 对象请求进行签名，并且通过 SSL 连接发
   送给 OSS。 如果您设置了默认加密 SSE-KMS后，关注下客户端是否存在您更改前未失败但现在失败的 PUT 和 GET 请求，如果有这
   种情况，最可能是您未使用HTTPS协议。

3.点击确定，完成设置。

## 默认加密用于数据同步
在为数据同步的目标存储空间启用默认加密后，将应用以下加密行为：

如果您设置的目标存储桶开启默认加密，无论是源存储空间中的对象是否进行加密，OSS都将对目标存储桶中的副本对象进行加密。

**相关API参考**

-  设置存储空间默认加密  [PUT Bucket encryption](https://docs.jdcloud.com/cn/object-storage-service/put-bucket-encryption-2)
-  删除存储空间默认加密  [DELETE Bucket encryption](https://docs.jdcloud.com/cn/object-storage-service/delete-bucket-encryption-2)
-  获取存储空间默认加密设置  [GET Bucket encryption](https://docs.jdcloud.com/cn/object-storage-service/get-bucket-encryption-2)
