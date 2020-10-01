# automated puppet script to correct 500 error for Wordpress page.
exec { 'open file':
    command => 'vi /var/www/html/wp-settings.php'
}

exec { 'find and replace':
    command => sed -i 's/.phpp/.php/g' wp-settings.php
    require => Exec['open file']
}

package { 'apache2':
    ensure => 'installed'
}

exec { 'restart':
    command => 'sudo service apache2 restart'
    require => Package['apache2']
}
