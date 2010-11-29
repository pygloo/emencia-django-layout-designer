
YUI( { filter: 'debug' } ).use( 'bewype-layout-designer', function ( Y ) {

    var _hidden         = Y.one( 'input#content_id'),
        _fileStaticPath = Y.one( 'input#file_static_path').get( 'value' ),
        _uploadUrl      = Y.one( 'input#upload_url').get( 'value' ),
        CONTENT_NODE = Y.one( '#' + _hidden.get( 'value' ) );

    /**
     *
     */
    function attachNewsLetter () {

        // pug it
        CONTENT_NODE.plug( Y.Bewype.LayoutDesigner, {
            fileStaticPath  : _fileStaticPath,
            uploadUrl       : _uploadUrl,
            panelPosition   : 'right',
            panelOffsetY    : 40,
            panelOffsetX    : 40,
            pickerColorSize : 90
        } );
    }

    /**
     *
     */
    function onPreview ( e ) {

        // unplug before cloning;
        CONTENT_NODE.unplug( Y.Bewype.LayoutDesigner );

        // get clone for preview
        var _clone      = CONTENT_NODE.cloneNode( true ),
            _window     = null;

        // open window with content ...
        _window= window.open( '', 'previewWindow',
            'location=0, status=0, scrollbars=1, width=720, height=420' );
        // ..
        _window.document.write( '<center>' + _clone.get( 'innerHTML' ) + '</center>' );
        // re-attach
        attachNewsLetter( CONTENT_NODE );
    }

    /**
     *
     */
    function onSubmit( node ) {
    
        var _name       = node.get( 'name' ),
            _newsletter = Y.one( '#id_content' ),
            _textArea   = Y.Node.create( '<textarea id="id_content" name="content" />');

        // ..
        if ( [ '_addanother', '_continue', '_save' ].indexOf( _name ) != -1 && _newsletter ) {        
            // unplug before cloning;
            _newsletter.unplug( Y.Bewype.LayoutDesigner );
            // .. restore texte area
            _textArea.set( 'value', _newsletter.get( 'innerHTML' ) );
            // ..
            _newsletter.replace( _textArea );
            // hide textarea
            _textArea.setStyle( 'display', 'none' );
        }
    }

    /**
     *
     */
    function initLayoutDesignerEvents( submitRow ) {
        
        submitRow.all( 'input' ).each( function( v, k ) {

            var _target     = v,
                _type       = v.get( 'type' ),
                _name       = v.get( 'name' );

            // check is a submmit button
            if( _type === 'submit' ) {
                // .. add cb
                _target.after( 'click', function( e ) {
                    onSubmit( _target, _name );
                } );
            }
        } );
    }

    /**
     *
     */
    function initLayoutDesigner ( e ) {

        // get node
        attachNewsLetter();

        // .. add cb
        Y.one('#designer_preview').on( 'click', onPreview );

    }

    var _submitRow = Y.one( 'div.submit-row' );

    if ( _submitRow ) {    
        Y.after("domready", initLayoutDesigner );
        Y.after("domready", Y.bind( initLayoutDesignerEvents, this, _submitRow ) );
    }
} );

