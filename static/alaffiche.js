
getMovies();

function getMovies(){
	$.ajax({                                  
    url: "/api/allMovies/",
    dataType: "json",
  }).done(function(data) {
	  liste = data['result'];
	  document.getElementById('ListMovies').innerHTML =''
	  for (var i = 0; i < liste.length; i++) {
		  listMovies(liste[i],i+1);
	  }
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}


//function listMovies(movie,num){
	//document.getElementById('ListMovies').innerHTML += '<tr><td>'+num+'</td><td>'+movie[0]+
	//'</td><td>'+movie[1]+'</td><td>'+movie[2]+'</td><td>'+movie[3]+'</td><td>'+movie[4]+
	//'</td></td><td><a href="infoMovie.html?Id='+movie[5]+'"> <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-info-sign"></span></button></a></td></tr>' 
//}


function listMovies(movie,num){
	document.getElementById('ListMovies').innerHTML += '<tr><td>'+num+'</td><td><a href="infoMovie.html?Id='+movie[5]+'">'+movie[0]+
	'</a></td><td>'+movie[1]+'</td><td>'+movie[2]+'</td><td>'+movie[3]+'</td><td>'+movie[4]+
	'</td></tr>' 
}
