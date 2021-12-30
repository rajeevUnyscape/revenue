from django.shortcuts import render
import pandas as pd
import json
# Create your views here.

def index(request):
    # Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
    # Sample Header to extract

    # Manufacturer,Model,Sales in thousands,4-year resale value,Vehicle type,Price in thousands,Engine size,Horsepower,Wheelbase,Width,Length,Curb weight,Fuel capacity,Fuel efficiency,Latest Launch
    # Previous Header already working

    df = pd.read_csv("data/car_sales.csv")
    rs = df.groupby("Country")["Units Sold"].agg("sum")
    rs_pie = df.groupby("Region")["Units Sold"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)
    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content}
    return render(request, 'index.html', context=context)

def instant(request):
    df = pd.read_csv("data/car_sales.csv")
    df2 = pd.read_csv("data/tech.csv")
    rs = df.groupby("Country")["Units Sold"].agg("sum")
    rs_pie = df.groupby("Region")["Units Sold"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)
    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")

    table_content2 = df2.to_html(index=None)
    table_content2 = table_content2.replace("","")
    table_content2 = table_content2.replace('class="dataframe"',"id='big_tables2' class='lg table table-striped table-bordered'")
    table_content2 = table_content2.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content,'table_data2':table_content2}
    return render(request, 'instant.html', context=context)

def graphical(request):
    df = pd.read_csv("data/top_seller.csv")
    df2 = pd.read_csv("data/top_adds.csv")
    df3 = pd.read_csv("data/car_sales.csv")
    rs = df.groupby("country")["selling"].agg("sum")
    rs3 = df3.groupby("Country")["Units Sold"].agg("sum")
    rs_pie = df.groupby("country")["selling"].agg("sum")
    rs_pie2 = df2.groupby("country")["add"].agg("sum")

    categories = list(rs.index)
    values = list(rs.values)

    categories3 = list(rs3.index)
    values3 = list(rs3.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)
    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)
    data2 = []
    for index in range(0, len(rs_pie2.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie2.index[index], 'y': rs_pie2.values[index]  }
        data2.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values,"categories3": categories3, 'values3': values3, 'data': data, 'table_data':table_content,'data2': data2}
    return render(request, 'graphical.html', context=context)

def historical(request):
    df = pd.read_csv("data/car_sales.csv")
    rs = df.groupby("Country")["Units Sold"].agg("sum")
    rs_pie = df.groupby("Region")["Units Sold"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)
    data = []
    for index in range(0, len(rs_pie.index)):
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content}
    return render(request, 'historical.html', context=context)