jQuery(document).ready(function($) {
    handleTooltip();
	changeLocationOnCheckout();
    function handleTooltip() {
        $( document ).tooltip( { selector: '[ssb-toggle="tooltip"]' } );
    }

    (function(d) {
        var config = {
            kitId: 'nsl3tcs',
            scriptTimeout: 3000,
            async: true
        },
        h=d.documentElement,t=setTimeout(function(){h.className=h.className.replace(/\bwf-loading\b/g,"")+" wf-inactive";},config.scriptTimeout),tk=d.createElement("script"),f=false,s=d.getElementsByTagName("script")[0],a;h.className+=" wf-loading";tk.src='https://use.typekit.net/'+config.kitId+'.js';tk.async=true;tk.onload=tk.onreadystatechange=function(){a=this.readyState;if(f||a&&a!="complete"&&a!="loaded")return;f=true;clearTimeout(t);try{Typekit.load(config)}catch(e){}};s.parentNode.insertBefore(tk,s)
    })(document);

    function changeCartQuantity() {
        $('.woocommerce div.quantity').on( 'click', 'button.plus, button.minus', function() {
            console.log($(this));
            // Get current quantity values
            var qty = $( this ).closest( 'div.quantity' ).find( '.qty' );
            var val = parseFloat(qty.val());
            var max = parseFloat(qty.attr( 'max' ));
            var min = parseFloat(qty.attr( 'min' ));
            var step = parseFloat(qty.attr( 'step' ));
            
            // Change the value if plus or minus
            if ( $( this ).is( '.plus' ) ) {
                if ( max && ( max <= val ) ) {
                qty.val( max );
                }
                else {
                qty.val( val + step );
                }
            }
            else {
                if ( min && ( min >= val ) ) {
                    qty.val( min );
                } else if ( val > 1 ) {
                    qty.val( val - step );
                }
            }
    
            $(qty).change();
            
        });
    }

    $( document ).on( 'click', '#ssb-configurator-accordion-style .ssb-option', function(e){
        let href = $( this ).data( 'href' );
        if ($('.page-loading')[0]) {
            $('.page-loading').addClass('active');
        }
        location.href = href
    } )

    window.addEventListener('click', function( e ){
        if ( document.getElementById( 'shed-type-dropdown' ) && ! document.getElementById( 'shed-type-dropdown' ).contains( e.target ) ){
            $( '.dropdown-list' ).slideUp( 'fast' );
            $( '.shed-type-dropdown' ).removeClass( 'open' );
        }
    }); 

    changeCartQuantity();

    $( document.body ).on( 'updated_cart_totals', function() {
        changeCartQuantity();
    });

    $( '#mobile-custom-shed' ).on( 'click', function( e ){
        $( '.ssb-shed-product-single .summary-wrapper' ).addClass( 'active' );
    } )

    $( '.mobile-customize-panel .icon-close' ).on( 'click', function( e ){
        $( '.ssb-shed-product-single .summary-wrapper' ).removeClass( 'active' );
    } )

    $( '.shed-type-dropdown:not(.disabled) .current' ).on( 'click', function( ){
        $( this ).next( '.dropdown-list' ).slideToggle( 'fast' );
        $( '.shed-type-dropdown' ).toggleClass( 'open' );
    } )

    $( '.dropdown-list .dropdown-shed' ).on( 'click', function(){
        let id = $( this ).data( 'id' );
        let post_id = $( this ).data( 'post_id' );

        $( '.shed-type-dropdown' ).addClass( 'disabled' ).removeClass( 'open' );
        $( '.shed-type-dropdown .current' ).text( $( this ).text() );
        $( '#ssb-configurator-accordion-style .ssb-configurator-panel-content' ).addClass( 'loading' );
        $( '.dropdown-list' ).slideUp( 'fast' );        

        var data = {
            action: 'get_product_by_cat',
            cat_id : id,
            post_id : post_id,
        };

        jQuery.post(shedpro_data.ajax_url, data, function( response ) {
            $( '.shed-type-dropdown' ).removeClass( 'disabled' );
            $( '#ssb-configurator-accordion-style .ssb-configurator-panel-content' ).removeClass( 'loading' ).html( response );
        });
    } );

    window.addEventListener('click', function(e){
        var shed_type_dropdown = document.getElementById( 'shed-type-dropdown' );
        var popup_share = document.querySelector( '#popup-share-shed .wrap-share' );

        if ( shed_type_dropdown && ! shed_type_dropdown.contains( e.target ) ){
            $( '.dropdown-list' ).slideUp( 'fast' );
            $( '.shed-type-dropdown' ).removeClass( 'open' );
        }

        if ( popup_share && ! popup_share.contains( e.target ) ){
            $( '#popup-share-shed' ).removeClass( 'is_show' );
        }
        
    });

    $( '.saved-models-item .btn-share' ).on( 'click', function( e ){
        $( '#popup-share-shed' ).addClass( 'is_show' );

        let url = $( this ).data( 'url' );
        let modelUrl = $( this ).data( 'model-url' );
        $( '.list-share-social li' ).each( function( i, data ){
            $( data ).attr( 'data-url',url );
            $( data ).attr( 'data-model-url', modelUrl );
            $( data ).removeClass( 'shared' );
        } )

        return false;
    } )

    $('.list-share-social li.email').on('click',function(e){
        e.preventDefault();
        const _this = $(this);
        $( '#popup-share-shed' ).removeClass( 'is_show' );
        $( '#popup-form-contact-share' ).addClass( 'is_show' );
        $( '#popup-form-contact-share .wpcf7-not-valid-tip' ).remove();
        $( '#popup-form-contact-share .wpcf7-response-output' ).empty();
        $( '#popup-form-contact-share .wpcf7-form' ).removeClass( 'sent' );
        $( '#popup-form-contact-share .wpcf7-form' ).removeClass( 'failed' );
        $( '#popup-form-contact-share .wpcf7-form' ).removeClass( 'invalid' );
        $( '#popup-form-contact-share .wpcf7-form' ).addClass( 'init' );

        setTimeout( () => {
            const shareUrl  = _this.attr( 'data-url' );
            const modelUrl  = _this.attr( 'data-model-url' );
            $( '#popup-form-contact-share' ).find( '#share_url' ).val( shareUrl );
            $( '#popup-form-contact-share' ).find( '#model_url' ).val( modelUrl );
        },500 )
        
    });

    $( '.list-share-social li.copy_link' ).on( 'click', function() {
        const url = $( this ).attr( 'data-url' );
        $( this ).addClass( 'shared' );

        copyToClipboard( url );
    } );

    /**
     * Copy text to clipboard using the Clipboard API or a fallback method.
     * @param {string} text - The text to copy.
     * @returns {Promise<void>}
     */
    function copyToClipboard( text ) {
        if( navigator.clipboard && navigator.clipboard.writeText ) {
            return navigator.clipboard.writeText( text );
        }

        try {
            const textarea = document.createElement( 'textarea' );
            textarea.value = text;
            textarea.setAttribute( 'readonly', '' );
            textarea.style.position = 'absolute';
            textarea.style.left = '-9999px';
            document.body.appendChild( textarea );
            textarea.select();
            textarea.focus();
            document.execCommand( 'copy' );
            document.body.removeChild( textarea );
        } catch( err ) {
            console.error( 'Unable to copy text to clipboard:', err );
        }
    }

    $( '.remove-save-model' ).on( 'click', function( e ){        
        let _this = $( this );
        let id = _this.data( 'id' );
        $( '.list-saved-models' ).addClass( 'loading' );

        $.ajax({
            url: shedpro_data.ajax_url,
            dataType: 'JSON',
            method: 'POST',
            data: { action: 'remove_model', id: id }
            
        }).done(function( res ) {
            $( '.list-saved-models' ).removeClass( 'loading' );
            if( res.success ){
                _this.closest( '.saved-models-item' ).remove();
                if( res.count == 0 ) {
                    $('.nav-link.ssb-saved-models').removeClass('has-saved-models');
                } else {
                    $('.ssb-saved-models .icon-heart').attr( 'data-count',res.count );
                }
                
            }else{
                alert( res.msg );
            }
        });

        return false;
    } )

    $( '.share-shed .close-popup' ).on( 'click', function( e ) {
        $( this).parents( '.share-shed' ).removeClass( 'is_show' )

        return false;
    } );
    $( document ).on( 'click','#popup-form-contact-share .close-popup', function( ){
        $( '#popup-form-contact-share' ).removeClass( 'is_show' )

        return false;
    } );

    $('ul.list-product-cat').each(function(){
        if( screen.width <= 600 ){
            var list = $(this),
                select = $( document.createElement( 'select' ) ).insertBefore( $( this ).hide() ).change( function(){
                window.open( $( this ).val(), '_self' )
            });

            $('>li a', this).each( function(){
                select.attr( 'class', 'list-product-cat' );

                var option = $( document.createElement( 'option' ) )
                .appendTo( select )
                .val( this.href )
                .html( $( this ).html() );
                if( $( this ).hasClass( 'selected' ) ){
                    option.attr( 'selected', 'selected' );
                }
            });

            list.remove();
        }
    });

    $( '.list-share-social li' ).on( 'click', function( ){
        let _this = $(this);
        if( _this.hasClass('email') || _this.hasClass('copy_link') ) return;
        let winWidth    = 500;
        let winHeight   = 500;
        let winTop      = (screen.height / 2) - (winWidth / 2);
        let winLeft     = (screen.width / 2) - (winWidth / 2);
        let link        = _this.attr( 'href' );
        let url         = _this.data( 'url' );
        window.open(link + url, 'sharer', 'top=' + winTop + ',left=' + winLeft + ',toolbar=0,status=0,width='+winWidth+',height='+winHeight);
    } );

    /**
     * Set height for :root
     */
    var set_vh_root = function(){
        document.querySelector(':root').style
        .setProperty('--vh', window.innerHeight/100 + 'px');
    }
    
    set_vh_root();

    if ( $('select[data-plugin="select2"]')[0] ) {
        $('select[data-plugin="select2"]').selectWoo();
    }
    
    /**
     * Clear default data for checkout form
     */
    $( document ).on( 'click', '.clear-default-data', function( e ) {
        let form     = $( this ).closest( 'form' );
        let billing  = form.find( '.woocommerce-billing-fields' );
        let shipping = form.find( '.woocommerce-shipping-fields' );
        let popup    = form.find( '.popup-billing-fields__field-wrapper' );

        // Function to clear form fields
        function clearFields( container ) {
            // Clear input fields that are not readonly
            container.find( 'input.input-text:not( [readonly="readonly"] )' ).val( '' );
            setTimeout( () => {
                container.find( 'input#billing_state' ).addClass( 'input-text form-control input-lg' );
                container.find( 'input#shipping_state' ).addClass( 'input-text form-control input-lg' );
            }, 100 )
            
            // Clear select fields
            container.find( 'select' ).each( function() {
                if ( $( this ).find( 'option' ).length > 1 ) {
                    $( this ).val( '' ).trigger( 'change' );
                }
            } );

            // Clear checkbox fields
            container.find( 'input[type="checkbox"]' ).prop( 'checked', false ).trigger( 'change' );
        }

        // Clear billing and shipping fields
        clearFields( billing );
        clearFields( shipping );
        clearFields( popup );
        setTimeout( () => {
            $( '[name="billing_email"]' ).val( '' ).trigger( 'change' );
        }, 300 )
        
    } );

	/**
	 * Manages the "Change Location" functionality during the checkout process,
	 * allowing users to navigate to a product page and then trigger a specific
	 * action (like opening a zip code change modal) upon arrival.
	 *
	 * This function operates in two main phases:
	 * 1.  **Originating Page (Click Handler):**
	 *     - Listens for clicks on elements with the class `.checkout-change-location`.
	 *     - On click, it prevents the default link behavior.
	 *     - Retrieves the target URL from the `href` attribute of an anchor tag within `.product-shareable-link`.
	 *     - Sets a flag (`locationChangeTriggered = 'triggered'`) in `localStorage` to indicate a programmatic navigation.
	 *     - Redirects the user to the `targetPageUrl`.
	 * 2.  **Target Page (Page Load Logic):**
	 *     - On page load, it checks if the `locationChangeTriggered` flag is set in `localStorage`.
	 *     - If the flag is 'triggered', it simulates a click on the element with the ID `#change-zip-code`
	 *       (e.g., to open a zip code change modal or form).
	 *     - After triggering the action, it clears the `locationChangeTriggered` flag from `localStorage`
	 *       to prevent re-execution on subsequent direct visits.
	 *     - If the flag is not set, it assumes the page was accessed directly or the process was already completed.
	 *
	 * @function changeLocationOnCheckout
	 * @returns {void}
	 */
	function changeLocationOnCheckout() {
		$('.checkout-change-location').on('click', function (event) {
			event.preventDefault();
			const targetPageUrl = $('.product-shareable-link a').attr('href');
			const storageKey = 'locationChangeTriggered';
			// localStorage.setItem(storageKey, 'triggered');
			window.location.href = targetPageUrl + '&change-location=true';
		});

		const storageKey = 'locationChangeTriggered';
		const isTriggered = localStorage.getItem(storageKey);
		var queryString = window.location.search;
		var urlParams = new URLSearchParams(queryString);
		var changeLocation = urlParams.get('change-location');
		// if (isTriggered === 'triggered' && changeLocation == 'true') {
		if (changeLocation == 'true') {
			$('#change-zip-code').trigger('click');
			// localStorage.removeItem(storageKey);
		}
	}

});


Fancybox.bind("[data-fancybox]", {
	dragToClose: false,
	autoFocus: false,
	// click: function(){},
});

(function(){
    if( typeof fabric != 'undefined' ){
        var defaultOnTouchStartHandler = fabric.Canvas.prototype._onTouchStart;
        fabric.util.object.extend(fabric.Canvas.prototype, { 
            _onTouchStart: function(e) { 
                var target = this.findTarget(e); 
                if (this.allowTouchScrolling && !target && !this.isDrawingMode) { 
                    return; 
                } 
                defaultOnTouchStartHandler.call(this, e); 
            } 
        });
    }
})();

window.onload = ( event ) => {
    const $ = jQuery;
    getCookie = ( key ) => {
        const cookieKey     = `${key}=`;
        const decodedCookie = decodeURIComponent( document.cookie );
        let cookies         = decodedCookie.split( ';' );
        for( let i = 0; i < cookies.length; i++ ) {
            let cookie = cookies[i];
            while( cookie.charAt(0) == ' ') {
                cookie = cookie.substring( 1 );
            }

            if( cookie.indexOf( cookieKey ) == 0 ) {
                return cookie.substring( cookieKey.length, cookie.length );
            }
        }
        return false;
    }

    function addUrlParameter( name, value ) {
        const url = new URL( location );
        url.searchParams.set( name, value );
        history.pushState( {}, "", url );
    }

    const queryString = window.location.search;
	const urlParams = new URLSearchParams(queryString);
	const lotParam = shedpro_data?.location_configs?.param_and_cookie_lot ?? 'lot';
	const dealerParam = shedpro_data?.location_configs?.param_and_cookie_dealer ?? 'dealer';
	const dealer = urlParams.get(dealerParam);
	const lot = urlParams.get(lotParam);
	const dealerName = dealer ? dealer : getCookie(dealerParam);
	const lotName = lot ? lot : getCookie(lotParam);
	if ($('body').hasClass('enable-dealer-params')) {
		if (dealerName && '' !== dealerName) {
			addUrlParameter(dealerParam, dealerName);
		}
		if (lotName && '' !== lotName) {
			addUrlParameter(lotParam, lotName);
		}
	}

    window.addEventListener( 're-init-select2', event => {
        let locationID = event['detail'];
        $( '#ssb_order_office_to_contact_id' ).val( locationID ).select2();
    })

};