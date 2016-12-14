//Hide all provider divs
function hide_providers(){
    $('.provider').addClass('hidden');
}

//Hide all provider divs and show provider with given id
function show_provider(provider_id){
    var provider_div = '#provider_';
    provider_div = provider_div.concat(provider_id);
    hide_providers();
    $(provider_div).removeClass('hidden');
}
