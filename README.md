# xmlmerge

及搜客XML合并程序
这个程序已经封装成exe在Windows下可以直接运行<br />
其他说明：如下<br />
文件目录：<br />

-- exerun5.0 运行目录<br />
	-- xmlchange.exe  	可执行文件<br />
-- files	  			需处理的XML(递归子文件夹）<br />
	-- jingjie_详情_175894040_1117385545.xml<br />
	-- jingjie_详情_175894040_111738554f.xml<br />
	-- jingjie_详情_1758940s_1117385545.xml<br />
-- source    源程序<br />
	-- xmlchange.py		源代码<br />
	-- setup.py			打包配置<br />
--run.bat 批处理运行脚本
-- data  演示数据<br />

# 给非专业人士
使用方法：<br />

1.爬虫抓到的XML文件请放在files文件夹中<br />
  和运行目录exerun同一级，支持递归目录存放，只处理xml文件<br />

2.进入exerun5.0中运行xmlchange.exe|或者运行run.bat批处理脚本<br />

3.产生文件 “爬虫生成表”<br />

# 给专业人士
使用的python是3.4，且安装必须的python库
    pip3 install openpyxl
该库是2.35版本<br />
打包exe工具请安装cx_Freeze，然后进入source文件夹
    python setup.py build

# 版本信息
目前版本号为5.0
2015年11月27日版本修订<br />
1.下架的产品字段缺失，默认空<br />
2.新增线索ID和爬取时间等<br />
3.可能item出现嵌套情况，合并失败，<br />
  修复嵌套item<br />
4.提取item里面的属性值，支持多属性<br />
5.后继可增加新字段<br />

2015.12.14日版本修订<br />
1.递归检查子目录，深层合并<br />

# 疑问
疑问：<br />
请联系QQ：569929309<br />

一只尼玛
