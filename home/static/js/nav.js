$( '.navbar-nav a' ).on( 'click', function () {
	$( '.navbar-nav' ).find( 'li.active' ).removeClass( 'active' );
	$( this ).parent( 'li' ).addClass( 'active' );
});

$( '.navbar-nav a' ).on( 'click', function () {
  $(alert("Hello! I am an alert box!!");
}
