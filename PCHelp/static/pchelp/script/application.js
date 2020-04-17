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
	$(".parentspost").fadeOut(250);

	setTimeout(function(){
		$(".parentspost").attr("style", "display:none;");
	}, 250);

	//плавное появление карточки
	setTimeout(function(){
	$("#detailsblock").fadeIn(250);
	},250);

	}
}

//-----Правая сторона
//пока что выключили кнопку отправки формы
// document.getElementById('sendMail').onclick = function(event){
// 	event.preventDefault();
// };

$('#sendMail').on('click', function(){

	let inputname = document.getElementById("FirstName");
	let phoneinput = document.getElementById("phone");
	let messageiput = document.getElementById("message");
	let mistake = false; // переменная для наличия ошибки

	if (inputname.value.trim().length < 2){
		mistake = true;
		inputname.classList.add("mistakeform");
		inputname.title = "Слишком короткое имя!";
	}else {
		inputname.classList.remove("mistakeform");
		inputname.title = "";
	};

	if(phoneinput.value.trim().length != 16){
		mistake = true;
		phoneinput.classList.add("mistakeform");
		phoneinput.title = "Некорректный телефон!";
	}else {
		phoneinput.classList.remove("mistakeform");
		phoneinput.title = "";
	};

	if(messageiput.value.trim().length < 10){
		mistake = true;
		messageiput.classList.add("mistakeform");
		messageiput.title = "Описание должно содержать более 10 символов!";
	}else {
		messageiput.classList.remove("mistakeform");
		messageiput.title = "";
	};

	if (mistake){return}; //Если есть ошибка - возврат

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
