var path = require('path');
var webpack = require('webpack');


module.exports = {
    context: __dirname,
    entry: './bureau/static/js/main',
    output: {
        path: path.resolve('./bureau/static/bundles/'),
        filename: 'app.js'
    },

    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ],
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js',
            components: path.resolve(__dirname, 'bureau/static/js/components'),
        }
    },

};
