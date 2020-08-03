# puppet manifest to execute a command

exec {'killmenow':
    command  => 'pkill -TERM -f killmenow',
    provider => shell,
    returns  => 0,
}
