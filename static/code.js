
function update_echo(){
	var Name = $("#Nom_cinema").val();
	var City = $("#Ville").val();
	var Capacite = $("#Nbsalle").val();
	var Price = $("#Prix").val();
	
	$.ajax({                                  
    url: "/api/echo/",
    data: {
		Name: Name,
		City: City,
		Capacite: Capacite,
		Price: Price,
	},
	type: 'POST',
    dataType: "json",
  }).done(function(data) {
	 console.log("OK");
	 $("#texte-result").text("DONE");
  }).fail(function(args) {
	  console.warn('Bad request :', args);
	  $("#texte-result").text("(fail)");
  });
}

["#add-a", "#add-b"].forEach(function(item) {
  $(item).on("keyup", function(event) {
    // update_sum();
  });
});

["#add-mots"].forEach(function(item) {
  $(item).on("keyup", function(event) {
    // update_echo();
  });
});

["#my-form"].forEach(function(item) {
  $(item).on("submit", function(event) {
    update_echo();
  });
});
