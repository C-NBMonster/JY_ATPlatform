/**
 * 作者：吴俊威  日期：2018年9月
 */
function saveTable(tableID){
    var tableDict = {};
    var locator = $("#"+tableID+" tbody tr");
    var tableTrLength = locator.length;
    var tableTdLength = locator.parents().children().first().children().length;
    var tableDict = {"trLength":tableTrLength};
    for (var i=0; i<tableTrLength; i++){
        tableDict1=[];
        locatorTd = locator.children();
        for (var j=0; j<tableTdLength-1; j++){

            tableDict1[j]={"td":locatorTd.children().val()}
            locatorTd = locatorTd.next();
        }
        tableDict["tr"+i] = tableDict1;
        locator = locator.next();
    }
    return tableDict;
}
function comTable(id){
    var testsaveval = saveTable(id);
    $.ajax({
        type:'POST',
        url:"/param_save/",
        data:testsaveval,
        dataType:"json"
    });
}
function comTablea(id){
    var saveval = saveTable(id);
    $.ajax({
        type:'POST',
        url:"/cap_save/",
        data:saveval,
        dataType:"json"
    });
}
 function commitb()  {
     comTable("funcTable")
     layer.msg("保存成功");
     //alert('保存成功')
 }
 function commitba()  {
     comTablea("tablezjf")
     layer.msg("保存成功");
     //alert('保存成功')
 }
//function cTablec(id){
//    var savevalc = saveTable(id);
//    $.ajax({
//        type:'POST',
//        url:"/check_save/",
//        data:savevalc,
//        dataType:"json"
//    });
//}
//function ucommitc()  {
//     cTablec("checkTable")
//     layer.msg("保存成功");
// }
function add_trr(obj) {
//        alert("新增行方法1,新增行按钮写在备注前面");
         var tr=$(obj).parent().next().children().children().first().children().last();
         newTr = tr.clone();
         tr.after(newTr);
    $(".datepicker").datepicker({
        language: "zh-CN",
        autoclose: true,//选中之后自动隐藏日期选择框
        clearBtn: true,//清除按钮
        todayHighlight: true,
        format: "yyyy-mm-dd"//日期格式
        });
    newTr.find(".per_ip").bind("change",function(){
        changeServerIP(newTr.find(".per_ip"));
    });
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
function add_trr2(obj) {
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
function yx(the,id){
     layer.msg("已运行");
     //setTimeout(function(){window.location.reload();},1000);
     $("#"+id).attr({"disabled":true});
      $.ajax({
        url: "/run_apptest/",
        type:"POST",
        data:{"id":id},
        //async : false,  //异步
        success: function (e) {
            if(e=="运行完成"){layer.msg("运行完成");}
            else {layer.msg("运行异常");}
            $("#"+id).attr({"disabled":false});
            //window.location.reload();
    }
});
}

function runlive(the,id){
     layer.msg("已运行");
     //setTimeout(function(){window.location.reload();},1000);
     $("#"+id).attr({"disabled":true});
      $.ajax({
        url: "/run_livetest/",
        type:"POST",
        data:{"id":id},
        //async : false,  //异步
        success: function (e) {
            if(e=="运行完成"){layer.msg("运行完成");}
            else {layer.msg("运行异常");}
            $("#"+id).attr({"disabled":false});
            //window.location.reload();
    }
});
}


