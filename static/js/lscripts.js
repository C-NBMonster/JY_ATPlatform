/**
 * 作者：吴俊威  日期：2019年1月
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
function comTable(id,prm){
    var testsaveval = saveTable(id);
    $.ajax({
        type:'POST',
        url:"/"+prm+"/",
        data:testsaveval,
        dataType:"json"
    });
}
 function commitval(id,prm)  {
     comTable(id,prm)
     layer.msg("保存成功");
     //alert('保存成功')
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




