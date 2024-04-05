module.exports = {
    pages: {
        index: {
            entry: 'src/main.js',
            template: 'public/index.html',
            filename: 'index.html',
            title: 'FileTree',
            chunks: ['chunk-vendors', 'chunk-common', 'index']
        },
    },
    publicPath: './',
    configureWebpack: (config) => {
        if (process.env.NODE_ENV === 'production') {
            config.mode = 'production';
            config["performance"] = {
                "maxEntrypointSize": 10000000,
                "maxAssetSize": 30000000
            }
        }
    },
    devServer: {
        disableHostCheck: true,
    },
    lintOnSave: false,
}