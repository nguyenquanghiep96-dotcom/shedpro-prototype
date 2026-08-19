
    jQuery( document ).ready( function ( $ ) {
        var countertops = $('.group-countertops-color .ssb-configurator-group-name');
        var appliance   = $('.group-appliance-color .ssb-configurator-group-name');
        if( countertops[0] ) countertops.html( 'Countertops' );
        if( appliance[0] ) appliance.html( 'Cabinet Color' );
    } );
