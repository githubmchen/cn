# describeLogs


## 描述
获取日志文件列表<br>- 仅支持PostgreSQL, MySQL, Percona, MariaDB

## 请求方式
GET

## 请求地址
https://rds.jdcloud-api.com/v1/regions/{regionId}/instances/{instanceId}/log:describeLogs

|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**regionId**|String|True| |地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)|
|**instanceId**|String|True| |RDS 实例ID，唯一标识一个RDS实例|

## 请求参数
|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**pageNumber**|Integer|False| |显示数据的页码，默认为1，取值范围：[-1,∞)。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页;|
|**pageSize**|Integer|False| |每页显示的数据条数，默认为100，取值范围：[10,100]，用于查询列表的接口|
|**filters**|[Filter[]](describelogs#filter)|False| |过滤参数，多个过滤参数之间的关系为“与”(and)<br>支持以下属性的过滤：logType, 支持operator选项：eq, 仅支持 MySQL，Percona，MariaDB<br>|

### <div id="filter">Filter</div>
|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**name**|String|True| |过滤条件的名称|
|**operator**|String|False| |过滤条件的操作符，默认eq|
|**values**|String[]|True| |过滤条件的值|

## 返回参数
|名称|类型|描述|
|---|---|---|
|**result**|[Result](describelogs#result)| |

### <div id="result">Result</div>
|名称|类型|描述|
|---|---|---|
|**logs**|[Log[]](describelogs#log)| |
|**totalCount**|Integer| |
### <div id="log">Log</div>
|名称|类型|描述|
|---|---|---|
|**id**|String|日志文件id|
|**name**|String|日志文件名称|
|**sizeByte**|Integer|日志文件大小，单位Byte|
|**lastModified**|String|日志最后更改时间|
|**publicURL**|String|公网下载链接|
|**internalURL**|String|内网下载链接|

## 返回码
|返回码|描述|
|---|---|
|**200**|OK|

## 请求示例
GET
```
public void testDescribeLogs() {
    DescribeLogsRequest request = new DescribeLogsRequest();
    request.setInstanceId("mysql-k67q8n46si");
    request.setRegionId("cn-north-1");
    DescribeLogsResponse response = rdsClient.describeLogs(request);
    System.out.println(new Gson().toJson(response));
}

```

## 返回示例
```
{
    "requestId": "bpakejp25amgnp2oq5k40m07e0ghbjwm", 
    "result": {
        "logs": [
            {
                "id": "33083536-e9d8-463d-8f10-49b98d13a48c", 
                "lastModified": "2020-01-08T10:54:28", 
                "name": "mysql-slowlog-20200108_1054.log", 
                "sizeByte": 198
            }
        ], 
        "totalCount": 1
    }
}
```
