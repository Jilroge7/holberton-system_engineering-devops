# automated puppet script to correct 500 error for Wordpress page.
exec { 'find and replace':
    command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}
