/* global __dirname, require, module*/
const webpack = require('webpack');
const path = require('path');
const pkg = require('./package.json');
const CWP = require('clean-webpack-plugin');
const nodeExternals = require('webpack-node-externals');

module.exports = function (env) {
	const libraryName = pkg.name;
	const isProd  = env.prod === 1;
	const isWeb = env.target === 'web';
	const config = {
		mode: isProd ? 'production' : 'development',
		entry: __dirname + '/src/athlib.js',
    devtool: isProd ? false : 'source-map',
		output: {
			path: __dirname + (isWeb ? '/dist' : '/lib'),
			filename: libraryName + (isWeb ? '.web.js' : '.js'),
			library: libraryName,
			libraryTarget: 'umd',
			umdNamedDefine: true,
			globalObject: "typeof self !== 'undefined' ? self : this"
		},
		module: {
			rules: [
				{
					test: /(\.jsx|\.js)$/,
					loader: 'babel-loader',
					exclude: /(node_modules|bower_components)/
				},
				{
					test: /(\.jsx|\.js)$/,
					loader: 'eslint-loader',
					exclude: /node_modules/
				}
			]
		},
    optimization: {minimize: isProd},
    plugins: [],
		resolve: {
			modules: [path.resolve('./node_modules'), path.resolve('./src')],
			extensions: ['.json', '.js']
		}
	}
	var cwp = CWP;
	if (cwp.hasOwnProperty('CleanWebpackPlugin')) cwp = cwp.CleanWebpackPlugin;
  config.plugins.push(new cwp());
	return config;
}
