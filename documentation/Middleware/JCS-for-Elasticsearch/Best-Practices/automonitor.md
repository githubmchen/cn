## 监控告警配置建议
我们根据一些实际经验，提供了相对通用的告警配置建议，以供您参考。

指标 | 建议告警阈值 | 说明
:---: | :--- | :---
集群状态 |监控值连续10次>=2（即为红色）则报警 | 0 表示绿色，此时集群处于最健康状态；1 表示黄色，此时集群的高可用性受到影响，但是搜索结果仍然完整；2 表示红色，此时集群异常，搜索只能返回部分数据
节点磁盘使用率 | 最大值 连续10次>=75则报警（不要超过80%） | 磁盘使用率过高会导致数据无法正常写入
节点HeapMemory使用率 | 最大值 连续10次>=85则报警（不要超过90%） | 数值过高时影响查询性能
节点CPU使用率 | 最大值 连续10次>=95则报警 |CPU 使用率过高会导致集群节点处理能力下降，甚至宕机