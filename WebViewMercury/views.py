from django.shortcuts import render, redirect
from django.template.response import TemplateResponse


from django.http import HttpResponse
from .models import DBC, DBG, DBGC, DBPP, DBIC
from .forms import DBCForm, DBGForm, CheckFieldsDBIC, CheckCounter, FormDateRange
from django.utils import timezone
import datetime

import config as cfg

  
def index(request):
    # return HttpResponse("<h2>Главная</h2>")
    # return  TemplateResponse(request, "index.html")
    # data = {"name_counter_full": "Строительная сепарированная РП2", "net_adress": "81"}
    dbc = DBC.objects.all
    # return render(request, "wvm_template/index.html", context=data)
    data = {'dbc': dbc}
    # return render(request, "wvm_template/index.html", context=data)
    return render(request, "base.html", context=data)
 
# def about(request):
    # return HttpResponse("<h2>О сайте</h2>")
 
# def contact(request):
    # return HttpResponse("<h2>Контакты</h2>")

def page_counters(request):
    # return  TemplateResponse(request, "wvm_template/view_dbc.html")
    # data = {"name_counter_full": "Строительная сепарированная РП2", "net_adress": "81"}
    dbc = DBC.objects.all()
    data = {'dbc': dbc}
    print(data)
    # for item in dbc:
    #     print(item.name_counter_full)
    # for item in dbc:
    #     count_group = item.group.all().values_list()
    #     print(count_group)
        # for it in count_group:
        #     print(it.name_group_full)
            # item.group = it.name_group_full

    # return render(request, "wvm_template/view_dbc.html", context=data)
    return render(request, "view_dbc.html", context=data)

def view_dbg(request):
    dbg = DBG.objects.all
    data = {'dbg': dbg}
    return render(request, "view_dbg.html", context=data)




def page_profil_power(request):
    # datetime.datetime.now(tz=timezone.utc)
    if (cfg.date_range_start or cfg.date_range_stop) == None: 
        cfg.date_range_start = datetime.datetime.now()
        cfg.date_range_stop = datetime.datetime.now()
    if request.POST:
        form_DateRange = FormDateRange(request.POST)
        print(form_DateRange)
        if form_DateRange.is_valid():
            cfg.date_range_start = form_DateRange.cleaned_data['date_range_start']
            cfg.date_range_stop = form_DateRange.cleaned_data['date_range_stop']
            # print ("FormCleanedData:\n", form_DateRange.cleaned_data)
            print ("FormCleanedData:\n", cfg.date_range_start)
            print ("FormCleanedData:\n", cfg.date_range_stop)
            # dbpp = DBPP.objects.filter(datetime__range=(form_DateRange.cleaned_data['startDate'], form_DateRange.cleaned_data['endDate'])) & DBPP.objects.filter(counter=17)
            # form = DateRangeForm()
            # # form_DateRange['startDate'] = datetime.date(2023, 5, 1)
            # # form_DateRange['endDate'] = datetime.date(2023, 5, 25)
            # data = {'form': form,'dbpp': dbpp}
            # return render(request, "view_dbpp.html", context=data)
        else:
            print("upss_form_DateRange")
            print(form_DateRange)
            print(form_DateRange.cleaned_data)
            return redirect('view_dbpp')
    else:
        pass

    # dbpp = DBPP.objects.all()[:25]
    dbpp = DBPP.objects.filter(datetime__range=(cfg.date_range_start, cfg.date_range_stop)) & DBPP.objects.filter(counter=17)
    # dbpp = DBPP.objects.filter(datetime__range=('2023-05-01', '2023-05-25')) & DBPP.objects.filter(counter=17)
    form_DateRange = FormDateRange()
    # form_DateRange['startDate'] = datetime.date(2023, 5, 1)
    # form_DateRange['endDate'] = datetime.date(2023, 5, 25)
        # data = {'dbpp': dbpp}
    # return render(request, "wvm_template/view_dbc.html", context=data)
    # return render(request, "wvm_template/view_dbpp.html", context=data)
    # return  TemplateResponse(request, "view_dbpp.html")
    # valu = [48, -63, 81, 11, 70]
    # labels = ['January', 'February', 'March', 'April', 'May']
    contextD = {}
    contextD['data'] = [
            {
                'id': obj.id,
                'value': obj.P_plus,
                'date': obj.datetime.isoformat()

            }
            # for obj in DBPP.objects.all()[:25]
            for obj in DBPP.objects.filter(datetime__range=(cfg.date_range_start, cfg.date_range_stop)) & DBPP.objects.filter(counter=17)
        ]
    contextD['dbpp'] = dbpp
    contextD['daterange'] = form_DateRange
    # data = {'form': form_DateRange,
    #         'dbpp': dbpp,
    #         'data': }
    return render(request, "view_dbpp.html", context=contextD)




def page_view_dbic(request):
    if (cfg.date_range_start or cfg.date_range_stop) == None: 
            cfg.date_range_start = datetime.datetime.now()
            cfg.date_range_stop = datetime.datetime.now()
    if request.POST:
        if '_reload' in request.POST:
            # do_edit()
            # form_DateRange = DateRangeForm(request.POST)
            form_DateRange = FormDateRange(request.POST)
            print(form_DateRange)
            form_checkFieldsDBIC = CheckFieldsDBIC(request.POST)
            form_check_nameCounter = CheckCounter(request.POST)
            if form_checkFieldsDBIC.is_valid():
                a = form_checkFieldsDBIC.cleaned_data
                # print ("FormcheckFieldsDBIC:\n", a)
            else:
                print("upss_form_checkFieldsDBIC")
                # print(form_checkFieldsDBIC)
                # print(form_checkFieldsDBIC.cleaned_data)
                return redirect('view_dbic')
            if form_check_nameCounter.is_valid():
                b=form_check_nameCounter.cleaned_data
                name_counter = b['check_nameCounter']
                # print ("form_check_nameCounter:\n", name_counter)
                pk_counter = DBC.objects.get(name_counter_full=b['check_nameCounter']).pk
                # print(pk_counter)
            else:
                print("upss_form_check_nameCounter")
                # print(form_checkFieldsDBIC)
                # print(form_checkFieldsDBIC.cleaned_data)
                return redirect('view_dbic')
            
            if form_DateRange.is_valid():
                cfg.date_range_start = form_DateRange.cleaned_data['date_range_start']
                cfg.date_range_stop = form_DateRange.cleaned_data['date_range_stop']
                # print ("FormCleanedData:\n", form_DateRange.cleaned_data)
                print ("FormCleanedData:\n", cfg.date_range_start)
                print ("FormCleanedData:\n", cfg.date_range_stop)
                # print ("FormCleanedData:\n", form_checkFieldsDBIC.cleaned_data)
            #     # print("Form:\n", form_DateRange)
            #     dbpp = DBIC.objects.filter(datetime__range=(form_DateRange.cleaned_data['startDate'], form_DateRange.cleaned_data['endDate'])) & DBIC.objects.filter(counter=17)
            #     form = DateRangeForm()
            #     # form_DateRange['startDate'] = datetime.date(2023, 5, 1)
            #     # form_DateRange['endDate'] = datetime.date(2023, 5, 25)
            #     data = {'form': form,'dbic': dbic}
            #     return render(request, "view_dbic.html", context=data)
            else:
                print("upss_form_DateRange")
                print(form_DateRange)
                print(form_DateRange.cleaned_data)
                return redirect('view_dbic')
            # dbic = DBIC.objects.filter(datetime__range=('2023-04-24T00:00', '2023-05-30T00:00')) & DBIC.objects.filter(counter=pk_counter)
            dbic = DBIC.objects.filter(datetime__range=(cfg.date_range_start, cfg.date_range_stop)) & DBIC.objects.filter(counter=pk_counter)
            # print('dbic')
            # for item in dbic:
            #     print(item)
            # form_DateRange = DateRangeForm()
            # form_DateRange = FormDateRange()
            form_DateRange = FormDateRange()
            # form_DateRange_stop_date = FormDateRange()
            form_checkFieldsDBIC = CheckFieldsDBIC()
            form_check_nameCounter = CheckCounter()
            contextD = {}
            contextD['data'] = [
                    {
                        'id': obj.id,
                        'value1': obj.CurrentFaze1,
                        'value2': obj.CurrentFaze2,
                        'value3': obj.CurrentFaze3,
                        'value4': obj.CurrentSum,
                        'date': obj.datetime.isoformat()
                    }
                    # for obj in DBIC.objects.all()[:25]
                    for obj in DBIC.objects.filter(datetime__range=(cfg.date_range_start, cfg.date_range_stop)) & DBIC.objects.filter(counter=pk_counter)
                ]
            contextD['dbic'] = dbic
            contextD['form'] = form_checkFieldsDBIC
            contextD['fcnc'] = form_check_nameCounter
            # contextD['dt'] = form_DateRange
            contextD['daterange'] = form_DateRange
            # contextD['dt_stop'] = form_DateRange_stop_date
            contextD['lengend_graph'] = name_counter#+ '  '+ 'CurrentFaze1'
            return render(request, "view_dbic.html", context=contextD)


        elif '_inExcel' in request.POST:
            # do_delete()
            pass
    else:
        pass
    # if (date_range_start or date_range_stop) == None: date_range_start, date_range_stop = datetime.datetime.now()

    # dbic = DBIC.objects.all()[:25]
    dbic = DBIC.objects.filter(datetime__range=(cfg.date_range_start, cfg.date_range_stop)) & DBIC.objects.filter(counter=17)
    form_DateRange = FormDateRange()
    # form_DateRange_stop_date = FormDateRange()
    form_checkFieldsDBIC = CheckFieldsDBIC()
    form_check_nameCounter = CheckCounter()
    form_DateRange = FormDateRange()
    contextD = {}
    contextD['data'] = [
            {
                'id': obj.id,
                'value': obj.CurrentFaze1,
                'date': obj.datetime.isoformat()

            }
            # for obj in DBIC.objects.all()[:25]
            for obj in DBIC.objects.filter(datetime__range=(cfg.date_range_start, cfg.date_range_stop)) & DBIC.objects.filter(counter=17)
        ]
    contextD['dbic'] = dbic
    contextD['form'] = form_checkFieldsDBIC
    contextD['fcnc'] = form_check_nameCounter
    contextD['daterange'] = form_DateRange
    # contextD['dt_stop'] = form_DateRange_stop_date
    return render(request, "view_dbic.html", context=contextD)

# def add_counter(request):
#     # if request.metod == 'POST':
#     if request.POST:
        
#         form = DBCForm(request.POST)
#         # formdata = DateRangeForm(request.POST)
#         if form.is_valid():
#             print ("FormCleanedData:\n", form.cleaned_data)
#             # print("Form:\n", form)
#             # print("FormDate:\n", formdata)
#             # print(formdata.startDate)
#             # new_counter = DBC.objects.create(**form.cleaned_data)
#             # new_counter = form.save()
#             return redirect('view_dbc')
#         else:
#             print("upss")
#             print(form.cleaned_data)
#             return redirect('view_dbc')
#     else:
#         form = DBCForm()

#     dbc = DBC.objects.all
#     data = {}
#     data['dbc']= dbc
#     data['form']= form
#     # return render(request, "wvm_template/view_dbc.html", context=data)
#     return render(request, "add_counter.html", context=data)

def add_group(request):
    # if request.metod == 'POST':
    if request.POST:
        form = DBGForm(request.POST)
        if form.is_valid():
            # form.data['manuf_number'] = 123
            print (form.cleaned_data)
            print(form.data)
            print(form)
            # form.data['manuf_number'] = 123
            # print(form.data)
            # new_counter = DBC.objects.create(**form.cleaned_data)
            new_group = form.save()
            return redirect('view_dbc')
        else:
            print("upss...")
            print(form.cleaned_data)
            return redirect('view_dbc')
        pass
    else:
        form = DBGForm()

    data = {'form': form}
    # return render(request, "wvm_template/view_dbc.html", context=data)
    return render(request, "add_group.html", context=data)


def edit_counter(request):
    # if request.metod == 'POST':
    if request.POST:
        if '_buttonDeleteCounter' in request.POST:
            print(request.POST)
            id_counter = request.POST.get('_buttonDeleteCounter')
            # print(id_counter)
            DBC.objects.filter(pk=id_counter).delete()
            return redirect('view_dbc')
            # form = DBCForm(request.POST)
            # formdata = DateRangeForm(request.POST)
            # if form.is_valid():
            #     print ("FormCleanedData:\n", form.cleaned_data)
            #     # print("Form:\n", form)
            #     # print("FormDate:\n", formdata)
            #     # print(formdata.startDate)
            #     # new_counter = DBC.objects.create(**form.cleaned_data)
            #     # new_counter = form.save()
            #     DBC.objects.filter(pk=id_counter).delete()
            #     return redirect('view_dbc')
            # else:
            #     print("upss")
            #     print(form.cleaned_data)
            #     return redirect('view_dbc')
        if '_buttonEditCounter' in request.POST:
            # если нажата кнопка редактирования - данные строки переписываются в строку редактирования
            # print(request.POST)
            id_counter = request.POST.get('_buttonEditCounter')
            # print(id_counter)
            # counter = DBC.objects.filter(pk=id_counter)
            # counter = DBC.objects.get(pk=id_counter).net_adress
            # print(counter)
            data = {}

            form = DBCForm()
            # form.fields['id'].initial =  DBC.objects.get(pk=id_counter).pk
            cfg.id_edit_counter =  DBC.objects.get(pk=id_counter).pk
            form.fields['name_counter_full'].initial =  DBC.objects.get(pk=id_counter).name_counter_full
            form.fields['group'].initial =              DBC.objects.get(pk=id_counter).group
            form.fields['schem'].initial =              DBC.objects.get(pk=id_counter).schem
            form.fields['net_adress'].initial =         DBC.objects.get(pk=id_counter).net_adress
            form.fields['manuf_number'].initial =       DBC.objects.get(pk=id_counter).manuf_number
            form.fields['manuf_data'].initial =         DBC.objects.get(pk=id_counter).manuf_data
            form.fields['version_data'].initial =       DBC.objects.get(pk=id_counter).version_data
            form.fields['klass_react'].initial =        DBC.objects.get(pk=id_counter).klass_react
            form.fields['klass_act'].initial =          DBC.objects.get(pk=id_counter).klass_act
            form.fields['nom_u'].initial =              DBC.objects.get(pk=id_counter).nom_u
            form.fields['nom_i'].initial =              DBC.objects.get(pk=id_counter).nom_i
            form.fields['ku'].initial =                 DBC.objects.get(pk=id_counter).ku
            form.fields['ki'].initial =                 DBC.objects.get(pk=id_counter).ki
            form.fields['koefA'].initial =              DBC.objects.get(pk=id_counter).koefA
            data['form']= form
            if not (DBC.objects.get(pk=id_counter).manuf_data):
                    # print('upsssssssss')
                    form.fields['manuf_data'].initial = datetime.date(2000, 1, 1)
            # print(form)
            dbc = DBC.objects.all
            data['dbc']= dbc
            data['mode_edit'] = "update"
            
            return render(request, "edit_counter.html", context=data)

        if '_buttonSaveCounter' in request.POST:
            # если нажата кнопка записи торедактированноых данных - данные строки переписываются в DBC
            
            form = DBCForm(request.POST)
            # formdata = DateRangeForm(request.POST)
            if form.is_valid():
                # print ("FormCleanedData:\n", form.cleaned_data)
                # print("Form:\n", form)
                # print("FormDate:\n", formdata)
                # print(formdata.startDate)
                # new_counter = DBC.objects.create(**form.cleaned_data)
                # print(cfg.id_edit_counter)
                # update_counter = DBC.objects.get(pk=cfg.id_edit_counter)
                # update_counter.name_counter_full = 
                # form.fields['id'].initial =  cfg.id_edit_counter
                # update_counter.update()
                # print(form.cleaned_data['name_counter_full'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(name_counter_full=form.cleaned_data['name_counter_full'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(schem=form.cleaned_data['schem'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(net_adress=form.cleaned_data['net_adress'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(manuf_number=form.cleaned_data['manuf_number'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(manuf_data=form.cleaned_data['manuf_data'])
                # DBC.objects.filter(pk=cfg.id_edit_counter).update(version_data=form.cleaned_data['version_data'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(klass_react=form.cleaned_data['klass_react'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(klass_act=form.cleaned_data['klass_act'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(nom_u=form.cleaned_data['nom_u'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(nom_i=form.cleaned_data['nom_i'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(ku=form.cleaned_data['ku'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(ki=form.cleaned_data['ki'])
                DBC.objects.filter(pk=cfg.id_edit_counter).update(koefA=form.cleaned_data['koefA'])

                # new_counter = form.save()
                cfg.id_edit_counter = None
                return redirect('view_dbc')
            else:
                print("upss")
                # print(form.cleaned_data)
                return redirect('view_dbc')
        
        if '_addCounter'  in request.POST:
            form = DBCForm(request.POST)
            # formdata = DateRangeForm(request.POST)
            if form.is_valid():
                print ("FormCleanedData:\n", form.cleaned_data)
                # print("Form:\n", form)
                # print("FormDate:\n", formdata)
                # print(formdata.startDate)
                # new_counter = DBC.objects.create(**form.cleaned_data)
                new_counter = form.save()
                return redirect('view_dbc')
            else:
                print("upss")
                # print(form.cleaned_data)
                return redirect('view_dbc')

        # form = DBCForm()

        # dbc = DBC.objects.all
        # data = {}
        # data['dbc']= dbc
        # data['form']= form
        # # return render(request, "wvm_template/view_dbc.html", context=data)
        # return render(request, "add_counter.html", context=data)


    else:
        # перавый запрос страницы edit_counter.html
        form = DBCForm()
        form.fields['name_counter_full'].initial = 'новый счетчик'

    dbc = DBC.objects.all
    data = {}
    data['dbc']= dbc
    data['form']= form
    data['mode_edit'] = "add"
    print(dbc)
    # return render(request, "wvm_template/view_dbc.html", context=data)
    return render(request, "edit_counter.html", context=data)


def edit_group(request):
    # if request.metod == 'POST':
    if request.POST:
        if '_buttonDeleteGroup' in request.POST:
            print(request.POST)
            id_counter = request.POST.get('_buttonDeleteCounter')
            # print(id_counter)
            DBC.objects.filter(pk=id_counter).delete()
            return redirect('view_dbc')
            # form = DBCForm(request.POST)
            # formdata = DateRangeForm(request.POST)
            # if form.is_valid():
            #     print ("FormCleanedData:\n", form.cleaned_data)
            #     # print("Form:\n", form)
            #     # print("FormDate:\n", formdata)
            #     # print(formdata.startDate)
            #     # new_counter = DBC.objects.create(**form.cleaned_data)
            #     # new_counter = form.save()
            #     DBC.objects.filter(pk=id_counter).delete()
            #     return redirect('view_dbc')
            # else:
            #     print("upss")
            #     print(form.cleaned_data)
            #     return redirect('view_dbc')
        # if '_buttonEditCounter' in request.POST:
        #     # если нажата кнопка редактирования - данные строки переписываются в строку редактирования
        #     # print(request.POST)
        #     id_counter = request.POST.get('_buttonEditCounter')
        #     # print(id_counter)
        #     # counter = DBC.objects.filter(pk=id_counter)
        #     # counter = DBC.objects.get(pk=id_counter).net_adress
        #     # print(counter)
        #     data = {}

        #     form = DBCForm()
        #     # form.fields['id'].initial =  DBC.objects.get(pk=id_counter).pk
        #     cfg.id_edit_counter =  DBC.objects.get(pk=id_counter).pk
        #     form.fields['name_counter_full'].initial =  DBC.objects.get(pk=id_counter).name_counter_full
        #     form.fields['group'].initial =              DBC.objects.get(pk=id_counter).group
        #     form.fields['schem'].initial =              DBC.objects.get(pk=id_counter).schem
        #     form.fields['net_adress'].initial =         DBC.objects.get(pk=id_counter).net_adress
        #     form.fields['manuf_number'].initial =       DBC.objects.get(pk=id_counter).manuf_number
        #     form.fields['manuf_data'].initial =         DBC.objects.get(pk=id_counter).manuf_data
        #     form.fields['version_data'].initial =       DBC.objects.get(pk=id_counter).version_data
        #     form.fields['klass_react'].initial =        DBC.objects.get(pk=id_counter).klass_react
        #     form.fields['klass_act'].initial =          DBC.objects.get(pk=id_counter).klass_act
        #     form.fields['nom_u'].initial =              DBC.objects.get(pk=id_counter).nom_u
        #     form.fields['nom_i'].initial =              DBC.objects.get(pk=id_counter).nom_i
        #     form.fields['ku'].initial =                 DBC.objects.get(pk=id_counter).ku
        #     form.fields['ki'].initial =                 DBC.objects.get(pk=id_counter).ki
        #     form.fields['koefA'].initial =              DBC.objects.get(pk=id_counter).koefA
        #     data['form']= form
        #     if not (DBC.objects.get(pk=id_counter).manuf_data):
        #             # print('upsssssssss')
        #             form.fields['manuf_data'].initial = datetime.date(2000, 1, 1)
        #     # print(form)
        #     dbc = DBC.objects.all
        #     data['dbc']= dbc
        #     data['mode_edit'] = "update"
            
        #     return render(request, "edit_counter.html", context=data)

        # if '_buttonSaveCounter' in request.POST:
        #     # если нажата кнопка записи торедактированноых данных - данные строки переписываются в DBC
            
        #     form = DBCForm(request.POST)
        #     # formdata = DateRangeForm(request.POST)
        #     if form.is_valid():
        #         # print ("FormCleanedData:\n", form.cleaned_data)
        #         # print("Form:\n", form)
        #         # print("FormDate:\n", formdata)
        #         # print(formdata.startDate)
        #         # new_counter = DBC.objects.create(**form.cleaned_data)
        #         # print(cfg.id_edit_counter)
        #         # update_counter = DBC.objects.get(pk=cfg.id_edit_counter)
        #         # update_counter.name_counter_full = 
        #         # form.fields['id'].initial =  cfg.id_edit_counter
        #         # update_counter.update()
        #         # print(form.cleaned_data['name_counter_full'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(name_counter_full=form.cleaned_data['name_counter_full'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(schem=form.cleaned_data['schem'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(net_adress=form.cleaned_data['net_adress'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(manuf_number=form.cleaned_data['manuf_number'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(manuf_data=form.cleaned_data['manuf_data'])
        #         # DBC.objects.filter(pk=cfg.id_edit_counter).update(version_data=form.cleaned_data['version_data'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(klass_react=form.cleaned_data['klass_react'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(klass_act=form.cleaned_data['klass_act'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(nom_u=form.cleaned_data['nom_u'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(nom_i=form.cleaned_data['nom_i'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(ku=form.cleaned_data['ku'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(ki=form.cleaned_data['ki'])
        #         DBC.objects.filter(pk=cfg.id_edit_counter).update(koefA=form.cleaned_data['koefA'])

        #         # new_counter = form.save()
        #         cfg.id_edit_counter = None
        #         return redirect('view_dbc')
        #     else:
        #         print("upss")
        #         # print(form.cleaned_data)
        #         return redirect('view_dbc')
        
        # if '_addCounter'  in request.POST:
        #     form = DBCForm(request.POST)
        #     # formdata = DateRangeForm(request.POST)
        #     if form.is_valid():
        #         print ("FormCleanedData:\n", form.cleaned_data)
        #         # print("Form:\n", form)
        #         # print("FormDate:\n", formdata)
        #         # print(formdata.startDate)
        #         # new_counter = DBC.objects.create(**form.cleaned_data)
        #         new_counter = form.save()
        #         return redirect('view_dbc')
        #     else:
        #         print("upss")
        #         # print(form.cleaned_data)
        #         return redirect('view_dbc')




    else:
        # перавый запрос страницы edit_group.html
        form = DBGForm()
        # form.fields['name_counter_full'].initial = 'новый счетчик'
    dbc = DBC.objects.all
    dbg = DBG.objects.all()
    dbgc = DBGC.objects.all
    data = {}
    data['dbc']= dbc
    data['dbg']= dbg
    data['dbgc']= dbgc
    data['form']= form
    data['mode_edit'] = "add"
    # count1 = DBC.objects.get(pk=1)
    # print(count1.group.all())
    # group1 = DBG.objects.get(pk=1)
    # # print(group1.counter_set.all())
    # print(DBGC.objects.get(group = DBG.objects.get(pk=1)))
    for item in dbg:
        print(item.name_group_full)
        print(item.counter_set.all)
    # return render(request, "wvm_template/view_dbc.html", context=data)
    return render(request, "edit_group.html", context=data)