$(function () {
    // 筛选数据
    $('#btn_query').click(function () {
        searchData();
    });

    $('#btn_delete').click(function () {
        var lines =  $("#tb_departments").bootstrapTable('getSelections');
        if (lines.length==0){
            alert("请选择一行数据！")
        } else{
            if (confirm("确定要删除吗？")) {
                for(var i=0;lines.length;i++){
                    $.ajax({
                        url: "/user/deleteUserTcpAddress/", data: {"id": lines[i].id}, async: false, success: function (result) {
                        }
                    });
                }
                searchData();
            }
        }
    });

    //1.初始化Table
    var oTable = new TableInit();
    oTable.Init();
});

function searchData() {
    $('#tb_departments').bootstrapTable('refresh');
}

var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_departments').bootstrapTable({
            url: '/user/getUserTcpAddress',         //请求后台的URL（*）
            method: 'get',                      //请求方式（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            pagination: true,                   //是否显示分页（*）
            sortable: false,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber:1,                       //初始化加载第一页，默认第一页
            pageSize: 10,                       //每页的记录行数（*）
            pageList: [10, 25, 50, 100],        //可供选择的每页的行数（*）
            search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
            strictSearch: true,
            showColumns: true,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
            height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "ID",                     //每一行的唯一标识，一般为主键列
            showToggle:true,                    //是否显示详细视图和列表视图的切换按钮
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            columns: [{
                checkbox: true
            },{
                field: 'id',
                title: 'id'
            }, {
                field: 'address',
                title: '地址'
            }, {
                field: 'connect',
                title: '连接状态',
                sortable: true,
                formatter: function (value, row, index) {
                    if (value) {
                       return '<span class="span_greem">已连接</span>';
                    }else {
                        return '<span class="span_gray">未连接</span>';
                    }
                }
            }, {
                field: 'createTime',
                title: '创建时间',
                sortable: true,
                //时间格式化
                formatter: function (value, row, index) {
                    return value.slice(0,19)
                }
            }, {
                field: '',
                title: '操作',
                sortable: true,
                formatter: function (value, row, index) {
                    var htmlStr =' <button class="btn btn-primary btn-xs" onclick="manipulate(\''+row.address+'\')">操控</button>';
                    //<button class="btn btn-danger btn-xs" onclick="delete_('+row.id+')">删除</button>
                    if (row.connect) {
                        return ' <button class="btn btn-warning btn-xs" onclick="connectClose(\''+row.address+'\')">断开连接</button>'+htmlStr;
                    }else {
                        return ' <button class="btn btn-success btn-xs" onclick="connect(\''+row.address+'\')">连接</button>'+htmlStr;
                    }
                }
            }, ]
        });
    };

    //得到查询的参数
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
            address: $("#txt_search_address").val(),
            startTime: $("#startTime").val(),
            endTime: $("#endTime").val()
            //statu: $("#txt_search_statu").val()
        };
        return temp;
    };
    return oTableInit;
};

function add() {
    var address=$("#address").val()
    if (address==''){
        alert ("地址不能为空！")
        return;
    }
    $.ajax({ url: "/user/addUserTcpAddress/",data:{"address":address},async:false, success: function(result){
            if (result.status=='Success'){
                $("tr[name$='data']").remove();
                refresh();
                $("#address").val('');
            }
        }});
}

function connect(address) {
    $.ajax({ url: "/connect/createTcpConnect/",data:{"address":address},async:false, success: function(result){
            if (result.status=='Success'){
                //$("tr[name$='data']").remove();
                searchData();
            }
        }});
}

function connectClose(address) {
    $.ajax({ url: "/connect/closeTcpConnect/",data:{"address":address},async:false, success: function(result){
            if (result.status=='Success'){
                //$("tr[name$='data']").remove();
                searchData();
            }
        }});
}

function manipulate(address) {
    url = "/manipulate/index/?address=" +address
    window.open(url);
}