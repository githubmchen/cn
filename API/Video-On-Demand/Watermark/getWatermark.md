# getWatermark


## 描述
查询水印

## 请求方式
GET

## 请求地址
https://vod.jdcloud-api.com/v1/watermarks/{watermarkId}

|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**watermarkId**|Long|True| |水印ID|

## 请求参数
无


## 返回参数
|名称|类型|描述|
|---|---|---|
|**result**|[Result](getwatermark#result)|查询水印结果|
|**requestId**|String|请求ID|

### <div id="result">Result</div>
|名称|类型|描述|
|---|---|---|
|**id**|Long|水印ID|
|**name**|String|水印名称。只支持中英文、数字。长度不超过128个字符。UTF-8编码。<br>|
|**imgUrl**|String|图片地址|
|**width**|String|水印宽度。<br>当 sizeUnit = pixel 时，取值范围为 [8, 4096] 整数<br>当 sizeUnit = percent 时，取值范围为 [0, 100] 小数<br>|
|**height**|String|水印高度。<br>当 sizeUnit = pixel 时，取值范围为 [8, 4096] 整数<br>当 sizeUnit = percent 时，取值范围为 [0, 100] 小数<br>|
|**sizeUnit**|String|尺寸单位。取值范围：<br>  pixel - 像素<br>  percent - 百分比<br>默认值为 pixel<br>|
|**position**|String|水印位置。取值范围：<br>  LT - 左上<br>  RT - 右上<br>  LB - 左下<br>  RB - 右下|
|**offsetX**|String|水平偏移。<br>当 offsetUnit = pixel 时，取值范围为 [8, 4088] 整数<br>当 offsetUnit = percent 时，取值范围为 [0, 100] 小数<br>|
|**offsetY**|String|竖直偏移。<br>当 offsetUnit = pixel 时，取值范围为 [8, 4088] 整数<br>当 offsetUnit = percent 时，取值范围为 [0, 100] 小数<br>|
|**offsetUnit**|String|偏移单位。取值范围：<br>  pixel - 像素<br>  percent - 百分比<br>默认值为 pixel<br>|
|**createTime**|String|创建时间|
|**updateTime**|String|修改时间|

## 返回码
|返回码|描述|
|---|---|
|**200**|OK|
|**400**|Invalid parameter|
|**401**|Authentication failed|
|**404**|Not found|
|**500**|Internal server error|
|**503**|Service unavailable|

## 请求示例
GET
```
https://vod.jdcloud-api.com/v1/watermarks/1

```

## 返回示例
```
{
    "requestId": "edfc74ea-be4c-418b-b841-31ddd2b33203", 
    "result": {
        "createTime": "2019-04-16T15:51:32Z", 
        "height": 50, 
        "id": 1, 
        "imgUrl": "http://s3.cn-north-1-stag.jcloudcs.com/vod-storage-72757/image/ecd9066c0f2c8e4bbd8a9fd7ae37965f.PNG", 
        "name": "Mango", 
        "offsetX": 32, 
        "offsetY": 16, 
        "position": "LT", 
        "unit": "pixel", 
        "updateTime": "2019-04-16T15:51:32Z", 
        "width": 100
    }
}
```
