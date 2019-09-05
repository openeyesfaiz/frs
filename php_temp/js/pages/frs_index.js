var ws = new WebSocket("ws://fr.pop3global.com");


ws.onopen = function(evt){
	console.log('Open connection');
};

ws.onmessage = function(evt){
	console.log('Received message: ' + evt.data);
};

ws.onclose = function(evt){
	console.log('Connection closed.');
};

