jQuery(document).ready(function ($) {
    changeHeightConfiguratorTool();
    changeHeightConfiguratorTool_mobile();
    $(window).resize(function () {
        changeHeightConfiguratorTool();
        changeHeightConfiguratorTool_mobile();
    });

    addEventListener( 'show-price-change-zipcode', function( e ){
        changeHeightConfiguratorTool_mobile();
    } );

    $( document ).on( 'click','.icon-close, #mobile-custom-shed', function(){
        changeHeightConfiguratorTool();
        changeHeightConfiguratorTool_mobile();
    });

    $( document ).on( 'change', '#show-admin-price, .icon-close', function() {
        changeHeightConfiguratorTool();
        changeHeightConfiguratorTool_mobile();
    });

    function changeHeightConfiguratorTool() {
        if( $( window ).width() > 1024 ) {
            let height = 0;
            ['show-admin-price-wrap', 'wrap-price-add-to-cart','ssb-configurator-shed-type','pricing-disclaimer'].forEach( (e, i ) => {
                if( $( '.' + e ).length && $( '.' + e ).is( ":visible" ) ) {
                    const tmpHeight = $( '.'+e ).outerHeight( true ) || 0;
                    height += tmpHeight;
                }
            } );
            $('#ssb-configurator').css( 'height', 'calc(100% - ' + height+'px)');
        }
    }

    function changeHeightConfiguratorTool_mobile() {
        if ( $(window).width() < 1025 ) {
            // setTimeout(() => {
                const totalScreen       = $(".ssb-shed-product-single.woocommerce-page #content div.product div.summary").outerHeight( true );
                const shedTypeHeight    = $("#ssb-configurator-shed-type").outerHeight( true ) || 0;
                const mobilePanel       = $(".mobile-customize-panel").outerHeight( true ) || 0;
                const jPricingDisclaimer= $(".pricing-disclaimer");
                const pricingDisclaimer = jPricingDisclaimer.length && jPricingDisclaimer.is(":visible") ? jPricingDisclaimer.outerHeight( true ) || 0 : 7;
                const jAddToCart        = $(".wrap-price-add-to-cart");
                const addToCart         = jAddToCart.length && jAddToCart.is(":visible") ? jAddToCart.outerHeight( true ) || 0 : 0;
                const margin            = $('.pricing-disclaimer')[0] ? 20 : 0;
                const height            = addToCart + pricingDisclaimer - margin;
                $('.ssb-shed-product-single.woocommerce-page #content div.product div.summary').css('top', "calc(100% - " + height + "px)");
                $('.ssb-model-canvas-wrapper').css('height', "calc(100% - " + height + "px)");

                const zipCodeHeight = $('#change-zip-code').is(":visible") ? 40 : 20;
                const configHeight = totalScreen - ( shedTypeHeight + mobilePanel + pricingDisclaimer + addToCart + zipCodeHeight );

                $('#ssb-configurator').css('height', ( configHeight ) + "px");
            // }, 200);
            
        } else {
            $('.ssb-shed-product-single.woocommerce-page #content div.product div.summary, .ssb-model-canvas-wrapper').removeAttr('style');
        }
    }
    window.addEventListener( 'calculate-height', event => {
        if ( $(window).width() < 1025 ) {
            changeHeightConfiguratorTool_mobile();
        }
    });

    if( $("body").hasClass("dealer-show-button-price") ) {
        $( '.ssb-shed-product-single' ).addClass('dealer-button-price');
        getHeightShedDetail();
        $( window ).resize(function() {
            getHeightShedDetail();
        });
    }
    $( document ).on( 'click','.icon-close, #mobile-custom-shed', function(){
        getHeightShedDetail();
    });
    $( document ).on( 'change', '#show-admin-price, .icon-close', function() {
		const locationCookie =
			custom_script?.location_configs?.param_and_cookie_location ?? 'location';
		const zipCodeCookie = custom_script?.location_configs?.cookie_zip_code ?? 'zip-code';
		let zipCode =
			$('#js-select-location').length > 0
				? getCookie(locationCookie)
				: getCookie(zipCodeCookie);
        if( '' != zipCode && null != zipCode && 'continue' != zipCode ) {
            $( '.dealer-mode' ).toggleClass('hide-price');
            $( '.ssb-shed-product-single' ).toggleClass('dealer-show-price');
            $( '#ssb-configurator' ).toggleClass('dealer-show-price');
            getHeightShedDetail();
        }
        
    });
    function getCookie(cname) {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        for(let i = 0; i <ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
            c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
            }
        }
        return "";
    }
    function getHeightShedDetail() {
        if( ! $('#show-admin-price').length ) {
            return;
        }
        
        changeHeightConfiguratorTool();
        changeHeightConfiguratorTool_mobile();
    }

    /**
     * Clear dealer param value
     */
    $( document ).on( 'click', '#reset-dealer-param', function( e ) {
        $( this ).addClass( 'loading' );
    } );
    
});