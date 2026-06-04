jQuery(document).ready(function($) {
    if( screen.width <= 600 ){
        $( '.ssb-configurator-panel a').removeClass( 'ui-state-active ui-accordion-header-active' ).addClass( 'ui-accordion-header-collapsed' ).attr( 'aria-expanded', false ).attr( 'aria-selected', false );
        $( '.ssb-configurator-panel-content').removeClass( 'ui-accordion-content-active' ).slideUp().attr( 'aria-hidden', true );        
    }

    function setCookie(name,value,days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days*24*60*60*1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "")  + expires + "; path=/";
    }

    function getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
    }

    steps.filter( function( obj ){
        _width = window.screen.width;

        if( _width < 1025 ){
            delete obj.element;
            obj.position = 'auto';
        }

        return ! ( 'element' in obj ) || ( obj.element && $( obj.element ).length ) ;
    });

    let intro_step = {
        steps
    };

    $( document ).on( 'click', '.product-tour a', function( e ){        
        $( '.ssb-configurator-panel a').removeClass( 'ui-state-active ui-accordion-header-active' );
        $( '.ssb-configurator-panel-content').removeClass( 'ui-accordion-content-active' ).slideUp();

        introJs().setOptions( intro_step ).start();

        return false
    } );

    const productTour                   = getCookie( 'is_show_product_tour' );
    const disableFirstLoadProductTour   = ssb_product_tour.disable_first_load_product_tour == 1;

    if( $( 'body' ).hasClass( 'ssb-shed-product-single' ) && ! productTour && ! disableFirstLoadProductTour ){
        introJs().setOptions( intro_step ).start();
        setCookie( 'is_show_product_tour', true, 365 );
    }
});