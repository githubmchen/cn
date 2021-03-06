# createImage


## 描述
为云主机创建私有镜像。云主机状态必须为<b>stopped</b>。<br>
云主机没有正在进行中的任务才可制作镜像。<br>
制作镜像以备份系统盘为基础，在此之上可选择全部或部分挂载数据盘制作整机镜像（如不做任何更改将默认制作整机镜像），制作镜像过程会为所挂载云硬盘创建快照并与镜像关联。<br>
调用接口后，需要等待镜像状态变为<b>ready</b>后，才能正常使用镜像。


## 请求方式
POST

## 请求地址
https://vm.jdcloud-api.com/v1/regions/{regionId}/instances/{instanceId}:createImage

|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**regionId**|String|True| |地域ID|
|**instanceId**|String|True| |云主机ID|

## 请求参数
|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**name**|String|True| |镜像名称，<a href="http://docs.jdcloud.com/virtual-machines/api/general_parameters">参考公共参数规范</a>。|
|**description**|String|False| |镜像描述，<a href="http://docs.jdcloud.com/virtual-machines/api/general_parameters">参考公共参数规范</a>。|
|**dataDisks**|[InstanceDiskAttachmentSpec[]](createimage#instancediskattachmentspec)|False| |数据盘列表，可以在实例已挂载数据盘的基础上，额外增加新的快照、空盘、或排除云主机中的数据盘。|

### <div id="instancediskattachmentspec">InstanceDiskAttachmentSpec</div>
|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**diskCategory**|String|False| |磁盘分类，取值为本地盘(local)或者云硬盘(cloud)。<br>系统盘支持本地盘(local)或者云硬盘(cloud)。系统盘选择local类型，必须使用localDisk类型的镜像；同理系统盘选择cloud类型，必须使用cloudDisk类型的镜像。<br>数据盘仅支持云硬盘(cloud)。<br>|
|**autoDelete**|Boolean|False| |是否随云主机一起删除，即删除主机时是否自动删除此磁盘，默认为true，本地盘(local)不能更改此值。<br>如果云主机中的数据盘(cloud)是包年包月计费方式，此参数不生效。<br>如果云主机中的数据盘(cloud)是共享型数据盘，此参数不生效。<br>|
|**cloudDiskSpec**|[DiskSpec](createimage#diskspec)|False| |数据盘配置|
|**deviceName**|String|False| |数据盘逻辑挂载点，取值范围：vda,vdb,vdc,vdd,vde,vdf,vdg,vdh,vdi,vmj,vdk,vdl,vdm|
|**noDevice**|Boolean|False| |排除设备，使用此参数noDevice配合deviceName一起使用。<br>创建整机镜像：如deviceName:vdb、noDevice:true，则表示云主机中的数据盘vdb不参与创建镜像。<br>创建模板：如deviceName:vdb、noDevice:true，则表示镜像中的数据盘vdb不参与创建主机。<br>创建主机：如deviceName:vdb、noDevice:true，则表示镜像中的数据盘vdb，或者模板(使用模板创建主机)中的数据盘vdb不参与创建主机。<br>|
### <div id="diskspec">DiskSpec</div>
|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**az**|String|True| |云硬盘所属的可用区|
|**name**|String|True| |云硬盘名称|
|**description**|String|False| |云硬盘描述|
|**diskType**|String|True| |云硬盘类型，取值为ssd、premium-hdd、ssd.gp1、ssd.io1、hdd.std1之一|
|**diskSizeGB**|Integer|True| |云硬盘大小，单位为 GiB，ssd 类型取值范围[20,1000]GB，步长为10G，premium-hdd 类型取值范围[20,3000]GB，步长为10G, ssd.gp1, ssd.io1, hdd.std1 类型取值均是范围[20,16000]GB，步长为10G|
|**iops**|Integer|False| |云硬盘IOPS的大小，当且仅当云盘类型是ssd.io1型的云盘有效，步长是10.|
|**snapshotId**|String|False| |用于创建云硬盘的快照ID|
|**charge**|[ChargeSpec](createimage#chargespec)|False| |计费配置；如不指定，默认计费类型是后付费-按使用时常付费|
|**multiAttachable**|Boolean|False| |云硬盘是否支持一盘多主机挂载，默认为false（不支持）|
|**encrypt**|Boolean|False| |云硬盘是否加密，默认为false（不加密）|
### <div id="chargespec">ChargeSpec</div>
|名称|类型|是否必需|默认值|描述|
|---|---|---|---|---|
|**chargeMode**|String|False|postpaid_by_duration|计费模式，取值为：prepaid_by_duration，postpaid_by_usage或postpaid_by_duration，prepaid_by_duration表示预付费，postpaid_by_usage表示按用量后付费，postpaid_by_duration表示按配置后付费，默认为postpaid_by_duration.请参阅具体产品线帮助文档确认该产品线支持的计费类型|
|**chargeUnit**|String|False| |预付费计费单位，预付费必填，当chargeMode为prepaid_by_duration时有效，取值为：month、year，默认为month|
|**chargeDuration**|Integer|False| |预付费计费时长，预付费必填，当chargeMode取值为prepaid_by_duration时有效。当chargeUnit为month时取值为：1~9，当chargeUnit为year时取值为：1、2、3|
|**autoRenew**|Boolean|False| |True=：OPEN——开通自动续费、False=CLOSE—— 不开通自动续费，默认为CLOSE|
|**buyScenario**|String|False| |产品线统一活动凭证JSON字符串，需要BASE64编码，目前要求编码前格式为 {"activity":{"activityType":必填字段, "activityIdentifier":必填字段}}|

## 返回参数
|名称|类型|描述|
|---|---|---|
|**result**|[Result](createimage#result)| |
|**requestId**|String| |

### <div id="result">Result</div>
|名称|类型|描述|
|---|---|---|
|**imageId**|String|镜像ID|

## 返回码
|返回码|描述|
|---|---|
|**200**|OK|
|**400**|Invalid parameter|
|**401**|Authentication failed|
|**404**|Not found|
|**429**|Quota exceeded|
|**500**|Internal server error|
|**503**|Service unavailable|
