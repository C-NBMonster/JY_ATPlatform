/**
 * 作者：吴俊威  日期：2019年1月
 **/
function add_trr3(obj) {
         var tr=$(obj).next().children().children().last();
         newTr = tr.clone();
         tr.after(newTr);
            $(".datepicker").datepicker({
            language: "zh-CN",
            autoclose: true,//选中之后自动隐藏日期选择框
            clearBtn: true,//清除按钮
            todayHighlight: true,
            format: "yyyy-mm-dd"//日期格式
        });
}
//$("#caseid").change(function() {
//  var id = $(this).val();
//  $.ajax({
//    url: '/ajax_c/',
//    data: {
//      'id': id,'runid':$('#runcaseid').val()
//    },
//    type: 'GET',
//    dataType: 'json',
//    success: function (data) {
//        $('#cnoid').val(data);
//    },
//  });
//});
 function cTablec(id){
    var savevalc = saveTable(id);
    $.ajax({
        type:'POST',
        url:"/check_save/",
        data:savevalc,
        dataType:"json"
    });
}
function ucommitc()  {
     cTablec("checkTable")
     layer.msg("保存成功");
 }
function deletetr(tdobject){
    var td=$(tdobject);
    var tableLength=td.parents().parents().children("tr").length;
    if (tableLength>1){
         td.parents("tr").remove();
    }else{
     deleteLastTr(tdobject);
}
}
function saveTable(tableID){
    var tableDict = {};
    var locator = $("#"+tableID+" tbody tr");
    var tableTrLength = locator.length;
    var tableTdLength = locator.parents().children().first().children().length;
    var tableDict = {"trLength":tableTrLength};
    for (var i=0; tableTrLength > i; i++){
        tableDict1=[];
        locatorTd = locator.children();
        for (var j=0; tableTdLength - 1 > j; j++){

            tableDict1[j]={"td":locatorTd.children().val()}
            locatorTd = locatorTd.next();
        }
        tableDict["tr"+i] = tableDict1;
        locator = locator.next();
    }
    return tableDict;}

function dbrun(){
     layer.msg("已运行");
     var mkid = $('#runcaseid').val();
      $.ajax({
        url: "/check_run/",
        type:"GET",
        data:{"mkid":mkid},
        dataType: 'json',
        success: function (e) {
            $('#checkdetail tbody').html('')
           for(i in e['check_run_list'])
            {
                if (e['check_run_list'][i][7]=='pass')
                {
                    ct = '<span style="color: #1ab394; font-size: 17px; font-weight: 600">pass</span>'
                }
                else {
                    ct = '<span style="color: #EE0000; font-size: 17px; font-weight: 600">fail</span>'
                }
                var tr;
                tr='<td>'+e['check_run_list'][i][0]+'</td>'+'<td>'+e['check_run_list'][i][1]+'</td>'+'<td>'+e['check_run_list'][i][2]+'</td>'+'<td>'+e['check_run_list'][i][3]+'</td>'+'<td>'+e['check_run_list'][i][4]+'</td>'+'<td>'+e['check_run_list'][i][5]+'</td>'+'<td>'+e['check_run_list'][i][6]+'</td>'+'<td>'+ct+'</td>'+'<td>'+e['check_run_list'][i][8]+'</td>'
                $("#checkdetail").append('<tbody>'+'<tr>'+tr+'</tr>'+'</tbody>')
            }
        layer.msg(e.da);
    }
});
}

function c(x){
    rowa = x.parentNode.parentNode.rowIndex
    var id = $(x).val();
    var table_w = document.getElementById("checkTable");
      $.ajax({
        url: '/ajax_c/',
        data: {
          'id': id,'runid':$('#runcaseid').val()
        },
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            table_w.rows[rowa].cells[1].innerHTML='<input id="cnoid" class="form-control" style="width:100px;" value="'+data+'"/>';
        },
      });
}