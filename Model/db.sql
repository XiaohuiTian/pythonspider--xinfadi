/*
Navicat MySQL Data Transfer

Source Server         : opensns
Source Server Version : 50619
Source Host           : 192.168.1.50:3306
Source Database       : sns

Target Server Type    : MYSQL
Target Server Version : 50619
File Encoding         : 65001

Date: 2017-03-23 18:12:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jpgk_news_goods
-- ----------------------------
DROP TABLE IF EXISTS `jpgk_news_goods`;
CREATE TABLE `jpgk_news_goods` (
  `id` varchar(32) NOT NULL COMMENT '主键',
  `name` varchar(50) NOT NULL COMMENT '商品名称',
  `category` int(11) NOT NULL COMMENT '商品分类(type=1,对应价格展示子分类id;type=2,对应新发地分类,从1开始)',
  `type` tinyint(3) NOT NULL DEFAULT '1' COMMENT '1:餐询网商品 2:新发地商品',
  `status` tinyint(3) NOT NULL DEFAULT '1' COMMENT '状态(-1--删除；0--禁用；1:可用;)',
  `unit` varchar(20) DEFAULT NULL,
  `buy_amount` int(10) NOT NULL DEFAULT '5' COMMENT '起购量',
  `description` text COMMENT '商品详情',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='价格展示分类下商品';

-- ----------------------------
-- Table structure for jpgk_news_goods_standard
-- ----------------------------
DROP TABLE IF EXISTS `jpgk_news_goods_standard`;
CREATE TABLE `jpgk_news_goods_standard` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(50) NOT NULL COMMENT '规格名称',
  `goods_id` varchar(32) NOT NULL COMMENT '商品id',
  `price` decimal(10,2) NOT NULL COMMENT '当日价',
  `lowest_price` decimal(10,2) DEFAULT NULL COMMENT '最低价',
  `highest_price` decimal(10,2) DEFAULT NULL COMMENT '最高价',
  `avg_price` decimal(10,2) DEFAULT NULL COMMENT '平均价',
  `difference_price` decimal(10,2) DEFAULT NULL COMMENT '较昨日差价',
  `unit` varchar(10) DEFAULT NULL COMMENT '单位',
  `status` tinyint(3) NOT NULL DEFAULT '1' COMMENT '状态(-1--删除；0--禁用；1:可用;)',
  `publish_date` date DEFAULT NULL COMMENT '发布时间',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `primary_key_index` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=37488 DEFAULT CHARSET=utf8 COMMENT='价格展示分类下商品规格';
