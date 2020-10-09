# automated puppet manifest to unlimit number of requests with nginx
exec { 'find and correct':
    command => "sed -i 's/ULIMIT=/# ULIMIT=/g' /etc/default/nginx",
    path    => [ '/usr/bin' , '/bin', '/usr/sbin', '/sbin' ],
}
exec { 'restart nginx':
    command => 'sudo service nginx restart',
    path    => '/usr/bin',
} ~>
service { 'nginx':
    ensure    => running,
}
