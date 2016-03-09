{% extends "rango/base.html" %}
{% load staticfiles %}
{% block content %}
<div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script>
	$(document).ready(function(){
		$("#p1").mouseleave(function(){
        alert("Bye! You now leave p1!");
    	});
	});
</script>
</head>
<body>
	<button>click</button>
	<p id="p1">This is a paragraph.</p>

</body>
</div>
{% endblock content %}