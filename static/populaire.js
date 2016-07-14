console.log('Hello Top');	

function printMoviesPopulaire(){
	var movies;
	$.ajax({                                  
    url: "/api/MoviesPopulaire/",
    dataType: "json",
    
  }).done(function(data) {
	 movies = data['result'];
	 document.getElementById('ListMoviesPopulaire').innerHTML =''
	 for (var i = 0; i < 10; i++) {
		 listMoviesGenre(movies[i],i+1);
	 }
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}


function listMoviesGenre(movie,num){
	console.log(movie);
	document.getElementById('ListMoviesPopulaire').innerHTML += '<tr><td>'+num+'</td><td><a href="infoMovie.html?Id='+movie[0]+'">'+movie[1]+
	'</a></td><td>'+movie[2]+'</td><td>'+movie[3]+'</td><td>'+movie[4]+'</td><td>'+movie[5]+'</td><td>'+movie[6]+
	'</td></tr>' 
}

printMoviesPopulaire();

