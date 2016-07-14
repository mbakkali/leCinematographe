console.log('Hello Genre');

$('#Action').click(function(e){
	e.preventDefault();
	var genre = 'Action';
	printMoviesGenre(genre);
});

$('#Animation').click(function(e){
	e.preventDefault();
	var genre = 'Animation';
	printMoviesGenre(genre);
});

$('#Comédie').click(function(e){
	e.preventDefault();
	var genre = 'Comedie';
	printMoviesGenre(genre);

});

$('#Drame').click(function(e){
	e.preventDefault();
	console.log('Drame');
	var genre = 'Drame';
	printMoviesGenre(genre);
	
});

$('#Erotic').click(function(e){
	e.preventDefault();
	var genre = 'Erotic';
	printMoviesGenre(genre);

});

$('#Romance').click(function(e){
	e.preventDefault();
	var genre = 'Romance';
	printMoviesGenre(genre);
	
});

$('#Science_Fiction').click(function(e){
	e.preventDefault();
	var genre = 'Science_Fiction';
	printMoviesGenre(genre);
});

$('#Thriller').click(function(e){
	e.preventDefault();
	var genre = 'Thriller';
	printMoviesGenre(genre);
});

$('#Tragedie').click(function(e){
	e.preventDefault();
	var genre = 'Tragedie';
	printMoviesGenre(genre);
});

function printMoviesGenre(genre){
	$('#div1').html("Recherche de film par genre: "+genre);
	var movies;
	$.ajax({                                  
    url: "/api/MoviesGenre/",
    data: {
		Genre: genre,
	},
    dataType: "json",
    
  }).done(function(data) {
	 movies = data['result'];
	 document.getElementById('ListMoviesGenre').innerHTML =''
	 for (var i = 0; i < movies.length; i++) {
		 listMoviesGenre(movies[i],i+1);
	 }
  }).fail(function(args) {
	  console.warn('Bad request :', args);
  });
}

//function listMovies(movie,num){
	//document.getElementById('ListMovies').innerHTML += '<tr><td>'+num+'</td><td>'+movie[0]+
	//'</td><td>'+movie[1]+'</td><td>'+movie[2]+'</td><td>'+movie[4]+
	//'</td></td><td><a href="infoMovie.html?Id='+movie[5]+'"> <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-info-sign"></span></button></a></td></tr>' 
//}


function listMoviesGenre(movie,num){
	console.log(movie);
	document.getElementById('ListMoviesGenre').innerHTML += '<tr><td>'+num+'</td><td><a href="infoMovie.html?Id='+movie[5]+'">'+movie[0]+
	'</a></td><td>'+movie[1]+'</td><td>'+movie[2]+'</td><td>'+movie[4]+
	'</td></tr>' 
}
