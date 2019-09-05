function del_u_record(u_id){
	//$.post("enrolled_detail.php?id=".concat(u_id),{del_hit_id:hit_id});
	console.log("DEL_U_RECORD func u_id is" + u_id);
	var url = 'enrolled_home.php';
	var form = $('<form action="' + url + '" method="post">' + '<input type="text" name="del_u_id" value="' + u_id + '">' + '</form>');
	$('body').append(form);
	form.submit();
}

function frs_u_delete(frs_host,u_ref_num,u_frsid){
	ws = new WebSocket(frs_host);
	console.log("FRSID is" + u_frsid);
	console.log("Ref Num is" + u_ref_num);
	
	ws.onopen = function(evt){
		query= '{"Detail":{"UserId":' + u_frsid + ',"Option":0},"RequestType":302,"RequestId":1}';
		console.log(query);
		ws.send(query);
	};
	
	ws.onclose = function(evt){
		ws = null
		//setTimeout(frs_update,5000)
	};
	
	ws.onmessage = function(evt){
		console.log(evt.data);
	};
	
	ws.onerror = function(evt){
		
	};
}