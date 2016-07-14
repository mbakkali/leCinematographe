
$('#Lyon').click(function(e){
	e.preventDefault();
	var ville = 'Lyon';
	printCinema(ville);
});

$('#Paris').click(function(e){
	e.preventDefault();
	var ville = 'Paris';
	printCinema(ville);
});

$('#Mulhouse').click(function(e){
	e.preventDefault();
	var ville = 'Mulhouse';
	printCinema(ville);
});


function printCinema(ville){
	$('#divville').html("Cinema a "+ville);
	
	$.ajax({                                  
    url: "/api/Cinemas/",
    data: {
		Ville: ville,
	},
    dataType: "json",
    
  }).done(function(data) {
	 console.log("ici");
	 var cinemas = data['result'];
	 document.getElementById('ListCinemas').innerHTML =''
	 for (var i = 0; i < cinemas.length; i++) {
		 listCinemas(cinemas[i],i+1);
	 }
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}

function listCinemas(cine,num){
	console.log("coucou");
	document.getElementById('ListCinemas').innerHTML += '<tr><td>'+num+'</td><td><a href="infoCine.html?Nom='+cine[0]+'">'+cine[0]+
	'</td><td>'+cine[1]+'</td><td>'+cine[2]+'</td>'
}
