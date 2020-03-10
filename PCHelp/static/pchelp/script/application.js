//---Левая сторона
//получаем все кнопки левой панели
var all = document.getElementById('left').children;

//Присваиваем каждой кнопке к событию клик функцию
for (let i in all){
	if (!all.hasOwnProperty(i) || i == 6) {
		continue;
	};

	all[i].onclick = function(event){

	//Получаем основную страницу карточки
	// передаем в неё параметр с какой кнопки был вызов
	// на стороне карточки подгружаем детальную информацию
	$.ajax({
		type: "POST",
		url:"detailblocks/main",
		data: {
			'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
			"Page":this.dataset['file']
		}, //тут информации с какой кнопки вызов и токен
		success: function(data){
			$("#detailsblock").html(data); //возвращаем в html
		}
	});


	//плавное исчезновение кнопок и задержка для дисплей none
	$(".parentspost").fadeOut(150);

	setTimeout(function(){
		$(".parentspost").attr("style", "display:none;");
	}, 150);

	//плавное появление карточки
	setTimeout(function(){
	$("#detailsblock").fadeIn(150);
	},150);

	}
}

//-----Правая сторона

//пока что выключили кнопку отправки формы
// document.getElementById('sendMail').onclick = function(event){
// 	event.preventDefault();
// };

$('#sendMail').on('click', function(){

	// event.preventDefault();

		$.ajax({
		type: "POST",
		url:"createbid",
		data: {
			'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
			'Firstname':$('#FirstName').val(),
			// 'Secondname':$('#Secondname').val(),
			'Phone':$('#phone').val(),
			//'Email':$('#email').val(),
			'Message':$('#message').val(),
			//'GroupSelect':$('#GroupSelect').val(),
		},
		//тут информации с какой кнопки вызов и токен
		 success: function(data){alert(data)}
	});

});
//console.log(all);