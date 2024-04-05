import json
import re

week_list = ('一', '二', '三', '四', '五', '六', '日')

day_list = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6}

course_data = dict()

week_data = {}

day_data = {}

for x in range(1, 20):
    week_data = dict()
    for y in week_list:
        day_data = dict()
        for z in range(1, 6):
            day_data[z] = 'null'
        week_data[y] = day_data
    course_data[x] = week_data

# 开始数据解析


print(str(json.dumps(course_data)))

raw_data = """<div class="mid_box">
					<div class="title">
						<p><font face="宋体"></font> 
							<!-- 查询得到的数据量显示区域 -->
						</p>
					</div>
					<!-- From内容 -->
					<span class="formbox" style="OVERFLOW:auto">
						<table class="datelist " cellspacing="0" cellpadding="3" border="0" id="DBGrid" width="98%">
	<tbody><tr class="datelisthead">
		<td>选课课号</td><td>课程代码</td><td>课程名称</td><td>课程性质</td><td>是否选课</td><td>教师姓名</td><td>学分</td><td>周学时</td><td>上课时间</td><td>上课地点</td><td>教材</td><td>修读标记</td><td>授课计划上传次数</td><td>授课计划最近上传时间</td><td>授课计划上传文件名</td><td>授课计划下载</td>
	</tr><tr>
		<td>(2022-2023-2)-AL091880-4158-1</td><td>AL091880</td><td><a href="html/kcxx/AL091880.html" target="_blank">现场总线技术</a></td><td>专业选修课程</td><td>是</td><td><a href="html/jsxx/4158.html" target="_blank">岳殿佐</a></td><td>2.5</td><td>4.0-0.0</td><td>
										<span id="DBGrid__ctl2_Label4">周四第1,2节{第1-11周};周四第1,2节{第13-16周};周四第3,4节{第13-16周};周四第3,4节{第11-11周|单周}</span>
									</td><td>A511;A511;;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl2$_ctl0','')">下载</a></td>
	</tr><tr class="alt">
		<td>(2022-2023-2)-AL092120-3062-1</td><td>AL092120</td><td><a href="html/kcxx/AL092120.html" target="_blank">手机移动开发技术</a></td><td>专业选修课程</td><td>是</td><td><a href="html/jsxx/3062.html" target="_blank">许娜</a></td><td>2.5</td><td>4.0-4.0</td><td>
										<span id="DBGrid__ctl3_Label4">周三第1,2节{第2-11周};周三第3,4节{第2-11周}</span>
									</td><td>A511;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl3$_ctl0','')">下载</a></td>
	</tr><tr>
		<td>(2022-2023-2)-AL151330-3075-1</td><td>AL151330</td><td><a href="html/kcxx/AL151330.html" target="_blank">形势与政策</a></td><td>公共通修课程</td><td>否</td><td><a href="html/jsxx/3075.html" target="_blank">杨松梅</a></td><td>0</td><td>2.0-0.0</td><td>
										<span id="DBGrid__ctl4_Label4">周五第7,8节{第6-9周}</span>
									</td><td>B104</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl4$_ctl0','')">下载</a></td>
	</tr><tr class="alt">
		<td>(2022-2023-2)-BS090490-2737-1</td><td>BS090490</td><td><a href="html/kcxx/BS090490.html" target="_blank">嵌入式课程教学实习</a></td><td>实践教学环节</td><td>否</td><td><a href="html/jsxx/2737.html" target="_blank">陈爽</a></td><td>2.0</td><td>+2</td><td>
										<span id="DBGrid__ctl5_Label4"></span>
									</td><td>&nbsp;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl5$_ctl0','')">下载</a></td>
	</tr><tr>
		<td>(2022-2023-2)-BS090540-3877-1</td><td>BS090540</td><td><a href="html/kcxx/BS090540.html" target="_blank">物联网系统企业实习</a></td><td>实践教学环节</td><td>否</td><td><a href="html/jsxx/3877.html" target="_blank">孙德杰</a></td><td>1.0</td><td>+1</td><td>
										<span id="DBGrid__ctl6_Label4"></span>
									</td><td>&nbsp;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl6$_ctl0','')">下载</a></td>
	</tr><tr class="alt">
		<td>(2022-2023-2)-BS090550-3062-1</td><td>BS090550</td><td><a href="html/kcxx/BS090550.html" target="_blank">手机移动开发课程教学实习</a></td><td>实践教学环节</td><td>否</td><td><a href="html/jsxx/3062.html" target="_blank">许娜</a></td><td>2.0</td><td>+2</td><td>
										<span id="DBGrid__ctl7_Label4"></span>
									</td><td>&nbsp;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl7$_ctl0','')">下载</a></td>
	</tr><tr>
		<td>(2022-2023-2)-AL093590-3877-1</td><td>AL093590</td><td><a href="html/kcxx/AL093590.html" target="_blank">数据处理与智能决策</a></td><td>专业核心课程</td><td>否</td><td><a href="html/jsxx/3877.html" target="_blank">孙德杰</a></td><td>2.0</td><td>4.0-4.0</td><td>
										<span id="DBGrid__ctl8_Label4">周一第5,6节{第1-11周};周一第5,6节{第13-13周|单周};周一第7,8节{第7-11周};周一第7,8节{第13-13周|单周}</span>
									</td><td>A507;A507;;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl8$_ctl0','')">下载</a></td>
	</tr><tr class="alt">
		<td>(2022-2023-2)-AL093600-3321-1</td><td>AL093600</td><td><a href="html/kcxx/AL093600.html" target="_blank">物联网工程设计与实施</a></td><td>专业核心课程</td><td>否</td><td><a href="html/jsxx/3321.html" target="_blank">张志广</a></td><td>2</td><td>4.0-4.0</td><td>
										<span id="DBGrid__ctl9_Label4">周二第1,2节{第8-9周};周二第1,2节{第2-7周};周二第3,4节{第2-9周}</span>
									</td><td>;A511;</td><td>1</td><td></td><td>&nbsp;</td><td>&nbsp;</td><td>未上传</td><td><a href="javascript:__doPostBack('DBGrid$_ctl9$_ctl0','')">下载</a></td>
	</tr>
</tbody></table>
					</span>
					<div class="footbox">
						<em class="footbox_con">
							<span class="pagination"></span>
							<span class="footbutton"></span>
							<!-- 底部按钮位置 -->
						</em>
					</div>
				</div>"""

pra = '<td>.*?</td><td>.*?</td><td><.*?" target="_blank">(.*?)</a></td><td>.*?</td><td>.*?</td><td><a href=".*?" target="_blank">.*?</a></td><td>.*?</td><td>.*?</td><td>'

course_name = re.findall(pra, raw_data)
for ss in course_name:
    print(ss)

pra = '<span id=".*?">(.*?)</span>'
course_time = re.findall(pra, raw_data)
for aa in course_time:
    print(aa)

index = {}

i = 0
for course in course_name:
    index[course] = course_time[i]
    i += 1

print(index)

for cou in course_name:
    print('课程名称', cou)
    print('上课时间')
    ppp = re.findall('周(.??)第(.*?),(.*?)节{第(.*?)-(.*?)周', index[cou], 0)
    for d in ppp:
        print(d)
        for week_index in range(int(d[3]), int(d[4]) + 1):
            print('第', week_index, '周')

            course_data[week_index][str(d[0])][day_list[int(d[1])]] = str(cou)

print(json.dumps({"a": course_data}))
print(course_data)
