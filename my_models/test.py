from datetime import datetime
from lunarcalendar import Converter, Solar, Lunar, YearType

def get_lunar_date(solar_date):
    # 将阳历日期转换为农历日期
    solar = Solar(solar_date.year, solar_date.month, solar_date.day)
    lunar = Converter.Solar2Lunar(solar)
    return lunar

def get_ganzhi_year(year):
    # 计算年份的天干地支
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    # 计算天干地支的索引
    stem_index = (year - 4) % 10
    branch_index = (year - 4) % 12
    
    return heavenly_stems[stem_index], earthly_branches[branch_index]

def get_ganzhi_month(year, month):
    # 计算月份的天干地支
    # 这里简化处理，实际计算需要考虑节气
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    earthly_branches = ["寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑"]
    
    # 计算天干地支的索引
    stem_index = (year * 12 + month - 3) % 10
    branch_index = (month - 3) % 12
    
    return heavenly_stems[stem_index], earthly_branches[branch_index]

def get_ganzhi_day(year, month, day):
    # 计算日期的天干地支
    # 这里简化处理，实际计算需要考虑具体的日干支表
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    # 计算天干地支的索引
    # 这里使用了一个简化的公式，实际计算需要更复杂的逻辑
    stem_index = (year * 12 + month * 31 + day - 3) % 10
    branch_index = (day - 3) % 12
    
    return heavenly_stems[stem_index], earthly_branches[branch_index]

def analyze_bazi(gender, birthdate, birthplace):
    # 解析阳历日期
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # 转换为农历日期
    lunar_date = get_lunar_date(birthdate)
    
    # 获取年、月、日的天干地支
    year_gan, year_zhi = get_ganzhi_year(lunar_date.year)
    month_gan, month_zhi = get_ganzhi_month(lunar_date.year, lunar_date.month)
    day_gan, day_zhi = get_ganzhi_day(lunar_date.year, lunar_date.month, lunar_date.day)
    
    # 获取生肖
    animals = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    year_animal = animals[(lunar_date.year - 4) % 12]
    
    # 获取五行属性
    elements = ["木", "火", "土", "金", "水"]
    year_element = elements[(lunar_date.year - 4) % 5]
    
    # 返回结果
    return {
        "gender": gender,
        "birthdate": birthdate.strftime("%Y-%m-%d"),
        "lunar_birthdate": f"{lunar_date.year}-{lunar_date.month}-{lunar_date.day}",
        "year_ganzhi": f"{year_gan}{year_zhi}",
        "month_ganzhi": f"{month_gan}{month_zhi}",
        "day_ganzhi": f"{day_gan}{day_zhi}",
        "year_animal": year_animal,
        "year_element": year_element
    }

# 示例调用
result = analyze_bazi("male", "1990-01-01", "Beijing")
print(result)