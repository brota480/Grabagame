from fabric.api import env
from fabric.operations import prompt

# Environments

def dev():
    "Development Settings"

    env.hosts = ['69.55.55.190']             # One or multiple server addresses in format ip:port
    env.Environment = 'dev'

    "Git Repository Settings"
    env.branch = 'develop'
    env.repo = 'git@github.com:chrismckinnel/Grabagame.git'

    "Application Paths"
    env.AppRoot = '/var/www/grabagame'

    "Build Settings"
    env.BuildName = 'dev'
    env.CacheDir = '/var/cache/grabagame'
    env.LogDir = '/var/log/grabagame'
    env.BuildRoot = '%(AppRoot)s/builds/dev' % env 
    env.DebugLevel = '1'

    "Domain Settings"
    env.BaseUrl = 'http://dev.grabagame.co.nz/'

    "Database settings"
    env.DatabaseName = 'Grabagame'
    env.DatabaseUser = 'Grabagame'
    env.DatabasePassword = 'ooge5viej3roo8shoo3voXeoquudaesh'

    "Other settings"
    env.Secret = 'Yeux3woo2aihi5ohrohtijup7fieCh7g'

def test():
    "Test Settings"

    env.hosts = ['69.55.55.190']             # One or multiple server addresses in format ip:port
    env.Environment = 'test'

    "Git Repository Settings"
    env.tag = prompt('Which release version do you want to deploy? [e.g: 1.1]')
    env.branch = 'release/%s' % env.tag
    env.repo = 'git@github.com:chrismckinnel/Grabagame.git'

    "Application Paths"
    env.AppRoot = '/var/www/grabagame'

    "Build Settings"
    env.BuildName = 'test'
    env.BuildRoot = '%(AppRoot)s/builds/test' % env 
    env.DebugLevel = '1'

    "Domain Settings"
    env.BaseUrl = 'http://test.grabagame.co.nz/'

def live():
    "Live Settings"

    env.hosts = ['69.55.55.190']             # One or multiple server addresses in format ip:port
    env.Environment = 'live'
    env.LuceneEnv = 'prod'

    "Git Repository Settings"
    env.tag = prompt('Which release version do you want to deploy? [e.g: v1.1]')
    env.branch = '%s' % env.tag
    env.repo = 'git@github.com:chrismckinnel/Grabagame.git'

    "Application Paths"
    env.AppRoot = '/var/www/grabagame'

    "Build Settings"
    env.BuildName = 'live'
    env.LastBuildRoot = '%(AppRoot)s/builds/live/latest' % env
    env.BuildRoot = '%(AppRoot)s/builds/live/%(tag)s' % env
    env.DebugLevel = '1'

    "Domain Settings"
    env.BaseUrl = 'http://grabagame.co.nz/'

