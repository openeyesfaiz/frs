
function del_record(u_id, hit_id){
	//$.post("enrolled_detail.php?id=".concat(u_id),{del_hit_id:hit_id});
	var url = 'enrolled_detail.php?id='.concat(u_id);
	var form = $('<form action="' + url + '" method="post">' + '<input type="text" name="del_hit_id" value="' + hit_id + '">' + '</form>');
	$('body').append(form);
	form.submit();
}

function frs_update(frs_host,u_id,u_name){
	ws = new WebSocket(frs_host);
	
	ws.onopen = function(evt){
		query= '{"Detail":{"User":{"Name":"",}}}'
		ws.send()
	};
	
	ws.onclose = function(evt){
		ws = null
		//setTimeout(frs_update,5000)
	};
	
	ws.onmessage = function(evt){
		
	};
	
	ws.onerror = function(evt){
		
	};
}
