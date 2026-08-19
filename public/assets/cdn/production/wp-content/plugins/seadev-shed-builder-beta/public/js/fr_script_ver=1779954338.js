jQuery(document).ready(function ($) {
	// Handle logout button on page load if user is logged in
	$('#ssb-floating-logout-button').on('click', function(e) {
		e.preventDefault();
		const $button = $(this);
		const originalText = $button.text();

		// Disable button and provide visual feedback
		$button.prop('disabled', true).text('Logging out...');

		$.ajax({
			url: fr_shedpro.ajax_url,
			method: 'POST',
			data: {
				action: 'handle_custom_logout',
			},
			success: function(response) {
				// Redirect if the server sends a redirect URL, otherwise just reload.
				if (response.success && response.data.redirect) {
					window.location.href = response.data.redirect;
				} else {
					window.location.reload();
				}
			},
			error: function(jqXHR) {
				console.error('Logout failed:', jqXHR.status, jqXHR.responseText);
				alert('An error occurred during logout. Please check the console for details.');
				// Re-enable the button and restore its original text on error
				$button.prop('disabled', false).text(originalText);
			}
		});
	});

	$('#ssb-floating-login-button').on('click', function () {
		$('#login-form').addClass('is_show');
	});
    $('#redirect_change_post_code').on('click',function(e){
        e.preventDefault();
        let url = $(this).attr('href');
        let ajaxurl = $(this).data('ajax_url');
        document.cookie = "zip-code=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        $.ajax({
            url: ajaxurl,
            method: 'GET',
            data : {
                action : "ssb_remove_cart_item",
                // type : 'remove'
            },
        }).done(function( res ) {
            window.location.href = url;
        });
    });

    function addMessageValid( element ) {
        element.addClass('validation');
        element.append( 'One or more fields have an error. Please check and try again.');
    }
    /**
     * show popup login
     */
     $( '.ssb-login-popup' ).on( 'click', function( e ){
        e.preventDefault();
        $( '#login-form .body-form-login h2' ).text( 'Login' );
        $( '#login-form' ).addClass( 'is_show' );
    } );
    
    /**
     * hide popup login
     */
    $( document ).on( 'click','.account-form .close-popup', async function(){
        $( '#login-form .btn.button').removeAttr('action');
        $( '#login-form' ).removeClass( 'is_show' );
    });

    /**
     * switch form login - register
     */
     $( document ).on( 'click','.account-form .link', async function(){
        let _this       = $(this);
        let _wrapform   = _this.parents('.wrap-form');
        let classname   = _this.attr('id');
        _wrapform.removeClass('login sign-up lost-password');
        _wrapform.addClass(classname);
        let message_box = _wrapform.find('.validate-message');
        message_box.removeClass('validation success');
    })
    
    $( document ).on( "click",".form-login .btn.button", function(e){
        e.preventDefault();
        call_ajax_login( $( this ) );
    });

    function call_ajax_login( currentElement, gRecaptcha = '') {
        const _this              = $( currentElement );
        const action             = _this.attr( 'action' );
        const _form              = _this.parents( '.form-login' );
        const username           = _form.find( '#username' ).val();
        const password           = _form.find( '#password' ).val();
        const remember           = _form.find( '#remember' ).is( ":checked" ) ? 'yes' : '';
        const message_box        = _form.find( '.validate-message');
        const element            = action === 'save' ? $('.ssb-save-model') : ( action === 'share' ? $('.ssb-share-model') : false );
        const isEnabledZonePrice = $( 'body.enable-zone-price' ).length ? true : false;
        message_box.empty();
        if( username === '' || password === '' ) {
            addMessageValid( message_box );
            return;
        }
        _this.addClass( 'loading' );
        $.ajax({
            url: fr_shedpro.ajax_url,
            dataType: 'JSON',
            method: 'POST',
            data: { 
                action:     'handle_login', 
                username:   username, 
                password:   password,
                remember:   remember,
				redirect: window.location.href,
            },
            success: function( res ) {
                _this.removeClass( 'loading' );
				$('#ssb-floating-login-button').addClass('hidden');
				const $logoutButton = $('#ssb-floating-logout-button');
				$logoutButton.removeClass('hidden');
                if( ! res.resp ) {
                    message_box.append( res.message);
                    message_box.addClass( 'validation' );
                } else {
					const locationCookie =
						fr_shedpro?.location_configs?.param_and_cookie_location ?? 'location';
					const zipCodeCookie =
						fr_shedpro?.location_configs?.cookie_zip_code ?? 'zip-code';
					const cookieKey =
						$('#js-select-location').length > 0 ? locationCookie : zipCodeCookie;
                    let zipCode = getCookie( cookieKey );
                    _form.find( '.validate-message' ).removeClass( 'validation' );
                    $( '#navbarNavDropdown' ).replaceWith( res.header );
                    $( '#navbarNavDropdown' ).removeClass( 'show' );
                    $( '.navbar .navbar-toggler' ).addClass( 'collapsed' );
                    $( '#wrapper-navbar .mobile-item' ).replaceWith( res.header_mobile );
                    $( '#login-form' ).removeClass( 'is_show' );
                    $( '.ssb-configurator-tools.action-save' ).replaceWith( res.configurator );
                    $( '.ssb-configurator-tools.ssb-tools-custom-line-items' ).replaceWith( res.custom_line );
                    $( '.ssb-save-btn' ).removeClass( 'not_login' );
                    $( '.ssb-share-model' ).removeClass( 'not_login' );
                    $( 'body' ).removeClass( 'no-logged' ).addClass( 'logged-in' );

                    if( res.can_view_building_type ) {
                        $( 'body' ).removeClass( 'not-view-building-type' );
                    }
                    if( res.can_see_est_price ) {
                        $( '.woocommerce .summary .wrap-title-price' ).removeClass( 'hide-price' );
                    }
                    if( 
                        ( res.can_see_est_price && '' != zipCode && zipCode && 'continue' != zipCode ) ||
                        ( res.can_see_est_price && ! isEnabledZonePrice )
                    ) {
                        $( '.woocommerce .summary .wrap-title-price .price' ).show();
                        $( 'body' ).addClass( 'show-price' );
                    }
                    if( res.can_see_net_price ) {
                        $( '#ssb-builder canvas' ).attr( 'data-show-net-price', true );
                        window.dispatchEvent( new CustomEvent( 'update-price-outside-ts' ) );
                        $( 'body' ).addClass( 'dealer-show-button-price' );
                        $('.woocommerce .summary .wrap-title-price .net-price').show();
                        $('.show-admin-price-wrap').removeClass( 'hidden' );
                    };
                    window.dispatchEvent( new CustomEvent( 'callback-after-login', { detail: { action: action, element: element, res: res } } ) );
                }
            },
        });
    }
    
    function call_ajax_register_account( element, gRecaptcha = '' ) {
        const _this         = element;
        const _form         = _this.parents('.form-sign-up');
        const username      = _form.find('#username_sigup').val();
        const email         = _form.find('#email').val();
        const phone         = _form.find('#phone').val();;
        const message_box   = _form.find('.validate-message');
        let urlRedirect     = _form.attr('redirect');
        message_box.removeClass('validation success');
        message_box.empty();
        if( username === '' || email === '' || phone === '' ) {
            addMessageValid( message_box );
            return;
        }
        if( ! urlRedirect ) {
            urlRedirect = window.location.href;
        }
        _this.addClass('loading');
        $.ajax({
            url: _this.data( 'ajax_url' ),
            dataType: 'JSON',
            method: 'POST',
            data: { 
                action: 'handle_register', 
                username: username, 
                email: email, 
                phone: phone,
                gRecaptcha: gRecaptcha,
                redirect: urlRedirect,
            }
            
        }).done( function( res ) {
            _this.removeClass('loading');
            if( !res.resp ){
                message_box.addClass('validation');
            }else{
                message_box.addClass('success');
            }
                message_box.append( res.message);
        })
    }
    /** handel signup  */
    $( document ).on( "click",".form-sign-up .btn.button", function(e){
        e.preventDefault();
        const _this         = $(this);
        if( $( '#recaptchaResponse' ).length ) {
            grecaptcha.ready(function () {
                grecaptcha.execute( ssbgRecaptcha.site_key  , { action: 'contact' } ).then( function ( token ) {
                   var recaptchaResponse    = document.getElementById( 'recaptchaResponse' );
                   recaptchaResponse.value  = token;
                   gRecaptcha               = token;
                   call_ajax_register_account( _this , gRecaptcha );
                } );
            } );
        } else {
            call_ajax_register_account( _this );
        }
    });

    /**
     * handle lost-password
     */
     $( document ).on( "click",".form-lost-password .btn.button", function(e){
        e.preventDefault();
        const _this             = $(this);
        const _form             = _this.parents('.form-lost-password');
        const username_email    = _form.find('#username_email').val();
        const message_box       = _form.find('.validate-message');
        message_box.removeClass('validation success');
        message_box.empty();
        if( username_email === '' ) {
            addMessageValid( message_box );
            return;
        }
        _this.addClass('loading');
        $.ajax({
            url: _this.data( 'ajax_url' ),
            dataType: 'JSON',
            method: 'POST',
            data: { 
                action: 'handle_lost_password', 
                username_email: username_email, 
            }
            
        }).done( function( res ) {
         _this.removeClass('loading');
            if( !res.resp ){
                message_box.addClass('validation');
            }else{
                message_box.addClass('success');
            }
             message_box.append( res.message);
        })
    });

    /**re-order */
    $( '.re-order' ).on('click',function( e ) {
        e.preventDefault();
        const url_config = $( this ).attr( 'href' );
        if( url_config !== '' ) {
            $('#popup-re-order .wrap-share').text("Double check your building's specs");
            $('#popup-re-order').addClass('is_show');
            setTimeout( function(){
                window.location.href = url_config;
            },2000)
        } else {
            $('#popup-re-order .wrap-share').text("This product is no longer available");
            $('#popup-re-order').addClass('is_show');
            setTimeout( function(){
                $('#popup-re-order').removeClass('is_show');
            },2000)
        }
       
	});

    /**send request to manufacturer */
    $( document ).on( 'click', '.send-to-MFR', function( e ) {
        e.preventDefault();
        const orderID   = $( this ).data( 'order' );
        const _this     = $( this );
        if( ! orderID ) return;
        const ajaxUrl = woocommerce_params.ajax_url;
        $( '#popup-send-to-mfr' ).addClass( 'is_show' );
        $( '#popup-send-to-mfr .response' ).empty();
        $( '#popup-send-to-mfr' ).removeClass( 'success' );
        $.ajax( {
            url:        ajaxUrl,
            dataType:   'JSON',
            method:     'POST',
            data: { 
                action: 'send_request_to_manufacturer', 
                orderID,
            }
        } ).done( function( res ) {
            if( res.success ) {
                $( '#popup-send-to-mfr' ).addClass( 'success' );
                $( '#popup-send-to-mfr .response' ).text( res.message );
                _this.prop( 'disabled', true );
                _this.text( "Order's sent to MFR", true );
            }
        } )
	} );


    /**
     * Switch show payment cash checkout form
     */
    $(document).on('click', '.switch-payment-cash li',function() {
        const _this = $(this);
        const type  = _this.attr('type');
        $('.switch-payment-cash li').removeClass('active');
        _this.addClass('active');
        if( type == 'cash-payment' ) {
            $('.order-total-monthly-payment').hide();
            $('.order-total').show();
        } else {
            $('.order-total-monthly-payment').show();
            $('.order-total').hide();
        }
    });

    $(document).on('click','.custom-number-month-select .selected', function( e ){
        const element = $(this);
        if( element.parent().hasClass('none-select')) return;
        
        if( element.hasClass('select-arrow-active') ){
             element.removeClass('select-arrow-active');
             element.siblings('.select-items-month').removeClass('show')
        } else {
             element.addClass('select-arrow-active');
             element.siblings('.select-items-month').addClass('show')
        }    
     })

     $(document).on('click','.select-items-month .item', function(){
         const element   = $(this);
         const financing = element.attr('custom-value');
         $('.select-items-month .item').removeClass('selected-item');
         element.addClass('selected-item');
         element.parent().removeClass('show');
         $('.custom-number-month-select .selected').text( financing );
         if( element.hasClass('checkout-form') ) {
            const monthly_payment = element.attr('monthly-payment');
            element.parents('.order-total-monthly-payment').find('.price-monthly').html( monthly_payment );
         } else {
             window.dispatchEvent( new CustomEvent( 'calculate_monthly_payment', {} ) );
         }
     });

     $(document).click(function(event) { 
         var $target = $(event.target);
         if(!$target.closest('.custom-number-month-select .selected').length ){
             $('.select-items-month').removeClass('show');
             $('.custom-number-month-select .selected').removeClass('select-arrow-active');
         }        
    });

    const isNumericInput = event => {
        const key = event.keyCode;
        return ( ( key >= 48 && key <= 57) || // Allow number line
            ( key >= 96 && key <= 105 ) // Allow number pad
        );
    };
    
    const isModifierKey = event => {
        const key = event.keyCode;
        return ( event.shiftKey === true || key === 35 || key === 36 ) || // Allow Shift, Home, End
            ( key === 8 || key === 9 || key === 13 || key === 46) || // Allow Backspace, Tab, Enter, Delete
            ( key > 36 && key < 41 ) || // Allow left, up, right, down
            (
                // Allow Ctrl/Command + A,C,V,X,Z
                ( event.ctrlKey === true || event.metaKey === true ) &&
                ( key === 65 || key === 67 || key === 86 || key === 88 || key === 90 )
            )
    };
    
    const formatToPhone = str => {
        let formatType = fr_shedpro.ssb_phone_number_format;
        if( ! formatType ) {
            formatType = 'domestic';
        }
        let result = '';
        if( 'domestic' === formatType ) {
            const input  = str.replace( /\D/g,'' ).substring( 0, 10 );
            const zip    = input.substring( 0,3 );
            const middle = input.substring( 3,6 );
            const last   = input.substring( 6,10 );
            if( input.length > 6 ){ 
                result = `(${zip})-${middle}-${last}`;
            } else if( input.length > 3 ){
                result = `(${zip})-${middle}`;
            } else if(input.length > 0 ){
                result = `(${zip}`;
            }
        } else if( 'local' === formatType ) {
            const input  = str.replace( /\D/g,'' ).substring( 0, 7 );
            const middle = input.substring( 0,3 );
            const last   = input.substring( 3,7 );
            if( input.length > 3 ){
                result = `${middle}-${last}`;
            } else if(input.length > 0 ){
                result = `${middle}`;
            }
        } else {
            const input   = str.replace( /\D/g,'' ).substring( 0, 11 );
            const country = input.substring( 0,1 );
            const zip     = input.substring( 1,4 );
            const middle  = input.substring( 4,7 );
            const last    = input.substring( 7,11 );
            if( input.length > 7 ){ 
                result = `+${country}-(${zip})${middle}-${last}`;
            } else if( input.length > 4 ){ 
                result = `+${country}-(${zip})${middle}`;
            } else if( input.length > 1 ){
                result = `+${country}-(${zip}`;
            } else if(input.length > 0 ){
                result = `+${country}`;
            }
        }

        return result;
    };

    const validTotalDigits = str => {
        if( '' === str ) return true;
        const formatType = fr_shedpro.ssb_phone_number_format;
        const phone      = str.replace( /\D/g,'' );
        let total        = 11;
        if( 'domestic' === formatType ) {
            total = 10;
        } else if( 'local' === formatType ) { 
            total = 7;
        }

        return '' === phone || phone.length < total;
    }

    $( document ).on( 'keydown', '#billing_phone', function( event ) {
        if( ! isNumericInput( event ) && ! isModifierKey( event ) ) {
            event.preventDefault();
        }
    } );

    $( document ).on( 'keyup', '#billing_phone', function( event ) {
        if( isModifierKey( event ) )  return;
        const value = $( this ).val();
        $( this ).val( formatToPhone( value ) );
    } );

    if( $( '#billing_phone' ).length ) {
        const value = $( '#billing_phone' ).val();
        $( '#billing_phone' ).val( formatToPhone( value ) );
    }
    const formatType = fr_shedpro.ssb_phone_number_format;
    let placeHolder  = '';

    if( 'international' === formatType ) {
        placeHolder = `+x-(xxx)xxx-xxxx`;
    } else if( 'local' === formatType ) {
        placeHolder = `xxx-xxxx`;
    } else {
        placeHolder = `(xxx)-xxx-xxxx`;
    }

    $( '#billing_phone' ).attr( 'placeholder', placeHolder );

    $( document ).on( 'click', '.accordion-cart-data .title', function() {
        const el    = $( this );
        const item  = el.parent();
        if( item.hasClass( 'active' ) ) {
            item.removeClass( 'active' );
            item.find( '.accordion-content' ).slideUp();
        } else {
            item.addClass( 'active' );
            item.find( '.accordion-content' ).slideDown();
        }
    } );

	if ($('#js-select-location').length > 0) {
		let count = 0;
		if( $('#js-select-location').find('option').length ) {
			$('#js-select-location').find('option').each(function() {
				const value = $(this).val();
				if (value !== null && value !== '') {
					count++;
				}
			});
		} else {
			count = jQuery('.wrap-locations-list .location-item').length;
		}
		if (count > 1) {
			jQuery('.footer-checkout #ssb_order_office_to_contact_name_field').append(
				'<div><a href="#" style="color:#ff7a00" id="change-office">Change location</a></div>',
			);
		}
	}

    jQuery( document ).on('click', '#change-office, #change-zipcode', function() {
        jQuery('.popup-checkout-footer .cancel-order').trigger('click');
        jQuery('#js-wrap-zip-code-popup').show();
    });

	var billing_zipcode = jQuery('.popup-billing-fields #billing_postcode_field #billing_postcode');
	if( billing_zipcode.length > 0 && billing_zipcode.attr('readonly') == 'readonly' ) {
		jQuery('.footer-checkout #billing_postcode_field').append(
			'<div><a href="#" style="color:#ff7a00" id="change-zipcode">Change ZIP Code</a></div>',
		);
	}
	
	if( typeof $( '#js-select-location' ).select2 !== "undefined" ) { 
		$( 'select#js-select-location' ).select2();
	}
	window.addEventListener( 're-init-select2-popup', event => {
       $( 'select#js-select-location' ).select2();
    })
   
});

jQuery(window).on('load', function ($) {
    const QAdomain = sessionStorage.getItem("QADomain");
    if( QAdomain && QAdomain != '' ) {
        var url = new URL(window.location.href);
        var search_params = url.searchParams;
        search_params.set('domain', QAdomain );
        url.search = search_params.toString();
        window.history.replaceState(null, null, '?'+url.toString().split('?')[1] );
    }
});

/**
 * Sends the current window's URL to the parent window via postMessage.
 * The message includes a source identifier ('shedpro_embed_viewer'), a message type ('shedpro_configurator_url'),
 * and the current URL. This function only executes if the current window has a parent and is not the top-level window.
 */
const sendUrlToParent = () => {
	if (window.parent && window.parent !== window) {
		const currentUrl = window.location.href;
		window.parent.postMessage(
			{
				message: 'shedpro_configurator_url',
				url: currentUrl,
			},
			'*',
		);
	}
};
sendUrlToParent();