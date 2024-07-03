create table whdserp_pro.ERP_BFXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    mtxx_id        bigint                             null comment '码头',
    mtbh           varchar(255)                       null,
    djzt           varchar(255)                       null,
    yxjr           varchar(255)                       null,
    txmy           varchar(255)                       null,
    queue          longtext                           null,
    bdmb           varchar(255)                       null,
    bdmb_width     decimal(18, 2)                     null comment '榜单宽度',
    bdmb_height    decimal(18, 2)                     null comment '榜单高度',
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null,
    lshqz          varchar(255)                       null,
    app_name       varchar(255)                       null,
    app_x          varchar(255)                       null,
    app_y          varchar(255)                       null,
    app_width      varchar(255)                       null,
    app_height     varchar(255)                       null,
    unit           varchar(255)                       null,
    constraint ERP_BFXX_lshqz_uindex
        unique (lshqz)
)
    comment '磅房信息';

create index ERP_BFXX_djzt_index
    on whdserp_pro.ERP_BFXX (djzt);

create index ERP_BFXX_lshqz_index
    on whdserp_pro.ERP_BFXX (lshqz);

create index ERP_BFXX_mtbh_index
    on whdserp_pro.ERP_BFXX (mtbh);

create index ERP_BFXX_mtxx_id_index
    on whdserp_pro.ERP_BFXX (mtxx_id);

create index ERP_BFXX_yxjr_index
    on whdserp_pro.ERP_BFXX (yxjr);


create table whdserp_pro.ERP_BHJL
(
    id             bigint auto_increment comment 'ID'
        primary key,
    bhlx           varchar(255)                       null,
    cjcz_id        bigint                             null comment '厂家厂址',
    ccgxx_id       bigint                             null comment '仓储罐',
    mtxx_id        bigint                             null comment '码头',
    czxx_id        bigint                             null comment '船只',
    cycgjl_id      bigint                             null comment '船运采购记录',
    hpxx_id        bigint                             null comment '货品信息',
    bhsj           datetime default CURRENT_TIMESTAMP null comment '备货时间',
    hplx           varchar(255)                       null,
    gg             varchar(255)                       null,
    pp             varchar(255)                       null,
    clxx_id        bigint                             null comment '车牌号',
    ddap_id        bigint                             null comment '订单安排ID',
    mz             decimal(18, 2)                     null comment '毛重',
    pz             decimal(18, 2)                     null comment '皮重',
    jz             decimal(18, 2)                     null comment '净重',
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null,
    nfhb           varchar(255)                       null,
    hbbh           varchar(255)                       null,
    split_from     bigint                             null comment '拆分源ID：备货记录ID',
    jszt           varchar(255)                       null,
    hb_code        bigint                             null,
    hb_primary_tag varchar(255)                       null
)
    comment '备货记录';

create index ERP_BHJL_bhlx_index
    on whdserp_pro.ERP_BHJL (bhlx);

create index ERP_BHJL_bhsj_index
    on whdserp_pro.ERP_BHJL (bhsj);

create index ERP_BHJL_ccgxx_id_index
    on whdserp_pro.ERP_BHJL (ccgxx_id);

create index ERP_BHJL_cjcz_id_index
    on whdserp_pro.ERP_BHJL (cjcz_id);

create index ERP_BHJL_clxx_id_index
    on whdserp_pro.ERP_BHJL (clxx_id);

create index ERP_BHJL_create_by_index
    on whdserp_pro.ERP_BHJL (create_by);

create index ERP_BHJL_create_time_index
    on whdserp_pro.ERP_BHJL (create_time);

create index ERP_BHJL_cycgjl_id_index
    on whdserp_pro.ERP_BHJL (cycgjl_id);

create index ERP_BHJL_czxx_id_index
    on whdserp_pro.ERP_BHJL (czxx_id);

create index ERP_BHJL_ddap_id_index
    on whdserp_pro.ERP_BHJL (ddap_id);

create index ERP_BHJL_gg_index
    on whdserp_pro.ERP_BHJL (gg);

create index ERP_BHJL_hb_code_index
    on whdserp_pro.ERP_BHJL (hb_code);

create index ERP_BHJL_hb_primary_tag_index
    on whdserp_pro.ERP_BHJL (hb_primary_tag);

create index ERP_BHJL_hplx_index
    on whdserp_pro.ERP_BHJL (hplx);

create index ERP_BHJL_hpxx_id_index
    on whdserp_pro.ERP_BHJL (hpxx_id);

create index ERP_BHJL_mtxx_id_index
    on whdserp_pro.ERP_BHJL (mtxx_id);

create index ERP_BHJL_pp_index
    on whdserp_pro.ERP_BHJL (pp);

create index ERP_BHJL_split_from_index
    on whdserp_pro.ERP_BHJL (split_from);

create index ERP_BHJL_update_by_index
    on whdserp_pro.ERP_BHJL (update_by);

create index ERP_BHJL_update_time_index
    on whdserp_pro.ERP_BHJL (update_time);

create table whdserp_pro.ERP_CCGXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    mc             varchar(255)                             null,
    fhdlx          varchar(255)                             null,
    dzxx           varchar(255)                             null,
    fhd            varchar(255)                             null,
    zdxx_id        bigint                                   null comment '站点',
    hplx           varchar(255)                             null,
    cpgg           varchar(255)                             null,
    dqdw           decimal(18, 2) default 0.00              null comment '当前吨位',
    zddw           decimal(18, 2) default 0.00              null comment '最大吨位',
    ccgzt          longtext                                 null,
    xm             varchar(255)                             null,
    dh             varchar(255)                             null,
    zw             varchar(255)                             null,
    djfz           varchar(255)                             null,
    create_by      varchar(255)                             null,
    create_time    datetime       default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                             null,
    update_time    datetime       default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                             null,
    data_key       varchar(255)                             null,
    authorized_key varchar(255)                             null,
    mtxx_id        bigint                                   null comment '关联码头的ID',
    glmt           varchar(255)                             null
)
    comment '仓储罐信息';

create table whdserp_pro.ERP_CJCZ
(
    id             bigint auto_increment comment 'ID'
        primary key,
    gys_id         bigint                             null comment '供应商',
    fkzh_id        bigint                             null,
    mc             varchar(255)                       null,
    fhdlx          varchar(255)                       null,
    dzxx           varchar(255)                       null,
    fhd            varchar(255)                       null,
    xm             varchar(255)                       null,
    dh             varchar(255)                       null,
    zw             varchar(255)                       null,
    djfz           varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '厂家厂址';

create index ERP_CJCZ_create_by_index
    on whdserp_pro.ERP_CJCZ (create_by);

create index ERP_CJCZ_create_time_index
    on whdserp_pro.ERP_CJCZ (create_time);

create index ERP_CJCZ_dzxx_index
    on whdserp_pro.ERP_CJCZ (dzxx);

create index ERP_CJCZ_fhd_index
    on whdserp_pro.ERP_CJCZ (fhd);

create index ERP_CJCZ_fhdlx_index
    on whdserp_pro.ERP_CJCZ (fhdlx);

create index ERP_CJCZ_gys_id_index
    on whdserp_pro.ERP_CJCZ (gys_id);

create index ERP_CJCZ_mc_index
    on whdserp_pro.ERP_CJCZ (mc);

create table whdserp_pro.ERP_CLXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    cph            varchar(255)                       null,
    gs             varchar(255)                       null,
    cz             varchar(255)                       null,
    khxx_id        varchar(255)                       null,
    dh             varchar(255)                       null,
    lx             varchar(255)                       null,
    gmrq           datetime                           null comment '购买日期',
    pc             varchar(255)                       null,
    nfjwx          varchar(255)                       null,
    wth            varchar(255)                       null,
    shzt           varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '车辆信息';

create index ERP_CLXX_cph_index
    on whdserp_pro.ERP_CLXX (cph);

create index ERP_CLXX_cz_index
    on whdserp_pro.ERP_CLXX (cz);

create index ERP_CLXX_gs_index
    on whdserp_pro.ERP_CLXX (gs);

create index ERP_CLXX_khxx_id_index
    on whdserp_pro.ERP_CLXX (khxx_id);

create index ERP_CLXX_lx_index
    on whdserp_pro.ERP_CLXX (lx);

create table whdserp_pro.ERP_DDAP
(
    id             bigint auto_increment comment 'ID'
        primary key,
    ddbh           varchar(255)                       null,
    bdbh           varchar(255)                       null,
    khxd_id        bigint                             null comment '订单',
    clxx_id        bigint                             null comment '车辆',
    fhdxx_id       bigint                             null comment '发货地ID',
    fhdlx          varchar(255)                       null,
    czxx_id        bigint                             null comment '船只ID',
    cycgjl_id      bigint                             null comment '船运采购记录ID',
    fkzh           bigint                             null comment '付款账户',
    apdw           decimal(18, 2)                     null comment '安排吨位',
    mz             decimal(18, 2)                     null comment '毛重',
    pz             decimal(18, 2)                     null comment '皮重',
    jz             decimal(18, 2)                     null comment '净重',
    fhddjxx_id     bigint                             null comment '发货地定价信息ID',
    ddap_je        decimal(18, 2)                     null comment '金额',
    dhzt           varchar(255)                       null,
    jdzt           varchar(255)                       null,
    finished       varchar(255)                       null,
    dd_finished    varchar(255)                       null,
    dzdw           decimal(18, 2)                     null comment '到站吨位',
    jz_auto        varchar(255)                       null,
    ycz            varchar(255)                       null,
    jdr_id         bigint                             null comment '接单人',
    bhjl_id        bigint                             null comment '备货记录ID',
    apsj           datetime default CURRENT_TIMESTAMP null comment '安排时间',
    jdsj           datetime                           null comment '接单时间',
    mzsj           datetime                           null comment '毛重时间',
    pzsj           datetime                           null comment '皮重时间',
    finish_time    datetime                           null comment '完成时间',
    colors         longtext                           null,
    yjs            varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null,
    hplx           varchar(255)                       null,
    cpgg           varchar(255)                       null,
    cppp           varchar(255)                       null,
    sbymc          varchar(255)                       null,
    zp_wc          longtext                           null,
    zp_mz          longtext                           null,
    zp_pz          longtext                           null,
    ddap_lx        varchar(255)                       null,
    hbbh           longtext                           null,
    hb_ddap_id     bigint                             null,
    hb_primary_tag varchar(255)                       null,
    mtxx_id        bigint                             null,
    color          varchar(255)                       null,
    sj_remark      varchar(255)                       null,
    constraint ERP_DDAP_ddbh_uindex
        unique (ddbh)
)
    comment '调度安排';

create index ERP_DDAP_apsj_index
    on whdserp_pro.ERP_DDAP (apsj);

create index ERP_DDAP_bdbh_index
    on whdserp_pro.ERP_DDAP (bdbh);

create index ERP_DDAP_bhjl_id_index
    on whdserp_pro.ERP_DDAP (bhjl_id);

create index ERP_DDAP_clxx_id_index
    on whdserp_pro.ERP_DDAP (clxx_id);

create index ERP_DDAP_cycgjl_id_index
    on whdserp_pro.ERP_DDAP (cycgjl_id);

create index ERP_DDAP_czxx_id_index
    on whdserp_pro.ERP_DDAP (czxx_id);

create index ERP_DDAP_ddap_lx_index
    on whdserp_pro.ERP_DDAP (ddap_lx);

create index ERP_DDAP_fhddjxx_id_index
    on whdserp_pro.ERP_DDAP (fhddjxx_id);

create index ERP_DDAP_fhddjxx_id_index_2
    on whdserp_pro.ERP_DDAP (fhddjxx_id);

create index ERP_DDAP_finished_index
    on whdserp_pro.ERP_DDAP (finished);

create index ERP_DDAP_fkzh_index
    on whdserp_pro.ERP_DDAP (fkzh);

create index ERP_DDAP_hb_ddap_id_index
    on whdserp_pro.ERP_DDAP (hb_ddap_id);

create index ERP_DDAP_jdr_id_index
    on whdserp_pro.ERP_DDAP (jdr_id);

create index ERP_DDAP_jdsj_index
    on whdserp_pro.ERP_DDAP (jdsj);

create index ERP_DDAP_jdzt_index
    on whdserp_pro.ERP_DDAP (jdzt);

create index ERP_DDAP_jdzt_index_2
    on whdserp_pro.ERP_DDAP (jdzt);

create index ERP_DDAP_khxd_id_index
    on whdserp_pro.ERP_DDAP (khxd_id);

create index ERP_DDAP_mtxx_id_index
    on whdserp_pro.ERP_DDAP (mtxx_id);

create index ERP_DDAP_yjs_index
    on whdserp_pro.ERP_DDAP (yjs);

create table whdserp_pro.ERP_FHJL
(
    id              bigint auto_increment comment 'ID'
        primary key,
    ddap_id         bigint                             null,
    khxx_id         bigint                             null comment '客户ID',
    zdxx_id         bigint                             null comment '站点ID',
    khxd_id         bigint                             null comment '订单ID',
    fhdxx_id        bigint                             null comment '发货地ID',
    fhdlx           varchar(255)                       null,
    czxx_id         bigint                             null comment '船只ID',
    cycgjl_id       bigint                             null comment '船运采购记录ID',
    hplx            varchar(255)                       null,
    cpgg            varchar(255)                       null,
    cppp            varchar(255)                       null,
    clxx_id         bigint                             null comment '车辆',
    mz              decimal(18, 2)                     null comment '毛重',
    pz              decimal(18, 2)                     null comment '皮重',
    jz              decimal(18, 2)                     null comment '净重',
    dzdw            decimal(18, 2)                     null comment '到站吨位',
    dj              decimal(18, 2)                     null comment '单价',
    hk              decimal(18, 2)                     null comment '货款',
    sj_id           bigint                             null comment '司机',
    apsj            datetime default CURRENT_TIMESTAMP null comment '安排时间',
    jdsj            datetime                           null comment '接单时间',
    mzsj            datetime                           null comment '毛重时间',
    pzsj            datetime                           null comment '皮重时间',
    finish_time     datetime                           null comment '完成时间',
    yjs             varchar(255)                       null,
    bhjl_id         bigint                             null comment '备货记录ID',
    create_by       varchar(255)                       null,
    create_time     datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by       varchar(255)                       null,
    update_time     datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark          varchar(255)                       null,
    data_key        varchar(255)                       null,
    authorized_key  varchar(255)                       null,
    hb_code         bigint                             null,
    hb_primary_tag  varchar(255)                       null,
    modified_byhand varchar(255)                       null,
    check_time      datetime                           null,
    check_state     varchar(255)                       null,
    check_level     varchar(255)                       null,
    check_info      longtext                           null
)
    comment '发货记录';

create index ERP_FHJL_apsj_index
    on whdserp_pro.ERP_FHJL (apsj);

create index ERP_FHJL_bhjl_id_index
    on whdserp_pro.ERP_FHJL (bhjl_id);

create index ERP_FHJL_check_level_index
    on whdserp_pro.ERP_FHJL (check_level);

create index ERP_FHJL_check_state_index
    on whdserp_pro.ERP_FHJL (check_state);

create index ERP_FHJL_check_time_index
    on whdserp_pro.ERP_FHJL (check_time);

create index ERP_FHJL_clxx_id_index
    on whdserp_pro.ERP_FHJL (clxx_id);

create index ERP_FHJL_create_by_index
    on whdserp_pro.ERP_FHJL (create_by);

create index ERP_FHJL_create_time_index
    on whdserp_pro.ERP_FHJL (create_time);

create index ERP_FHJL_cycgjl_id_index
    on whdserp_pro.ERP_FHJL (cycgjl_id);

create index ERP_FHJL_czxx_id_index
    on whdserp_pro.ERP_FHJL (czxx_id);

create index ERP_FHJL_ddap_id_index
    on whdserp_pro.ERP_FHJL (ddap_id);

create index ERP_FHJL_fhdxx_id_index
    on whdserp_pro.ERP_FHJL (fhdxx_id);

create index ERP_FHJL_finish_time_index
    on whdserp_pro.ERP_FHJL (finish_time);

create index ERP_FHJL_hb_code_index
    on whdserp_pro.ERP_FHJL (hb_code);

create index ERP_FHJL_hb_primary_tag_index
    on whdserp_pro.ERP_FHJL (hb_primary_tag);

create index ERP_FHJL_hplx_index
    on whdserp_pro.ERP_FHJL (hplx);

create index ERP_FHJL_khxd_id_index
    on whdserp_pro.ERP_FHJL (khxd_id);

create index ERP_FHJL_khxx_id_hplx_yjs_create_time_index
    on whdserp_pro.ERP_FHJL (khxx_id, hplx, yjs, create_time);

create index ERP_FHJL_khxx_id_index
    on whdserp_pro.ERP_FHJL (khxx_id);

create index ERP_FHJL_mzsj_index
    on whdserp_pro.ERP_FHJL (mzsj);

create index ERP_FHJL_pzsj_index
    on whdserp_pro.ERP_FHJL (pzsj);

create index ERP_FHJL_sj_id_index
    on whdserp_pro.ERP_FHJL (sj_id);

create index ERP_FHJL_update_by_index
    on whdserp_pro.ERP_FHJL (update_by);

create index ERP_FHJL_update_time_index
    on whdserp_pro.ERP_FHJL (update_time);

create index ERP_FHJL_yjs_index
    on whdserp_pro.ERP_FHJL (yjs);

create index ERP_FHJL_zdxx_id_index
    on whdserp_pro.ERP_FHJL (zdxx_id);

create table whdserp_pro.ERP_FHDDJXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    zddjxx_id      bigint                                   null comment '站点定价信息Id',
    fhd_id         bigint                                   null comment '发货地Id',
    fhdxx_id       bigint                                   null comment '发货地Id',
    fhdlx          varchar(255)                             null,
    xsj            decimal(18, 2)                           null comment '销售价',
    zccbj          decimal(18, 2)                           null comment '装车成本价',
    mlr            decimal(18, 2)                           null comment '毛利润',
    myzffs_id      bigint                                   null comment '支付方式',
    myzffscbje     decimal(18, 2) default 0.00              null comment '支付方式成本金额',
    mykpfs_id      bigint                                   null comment '开票方式',
    mykpfscbje     decimal(18, 2) default 0.00              null comment '开票方式成本金额',
    myzkje         decimal(18, 2) default 0.00              null comment '贸易折扣金额(元/吨)',
    yfykj          varchar(255)                             null,
    yfje           decimal(18, 2) default 0.00              null comment '运费金额',
    gls            decimal(18, 2) default 0.00              null comment '公里数',
    yfsfkp         varchar(255)                             null,
    yfkpcbje       decimal(18, 2) default 0.00              null comment '运费开票成本金额',
    qbfykj         varchar(255)                             null,
    qbfje          decimal(18, 2) default 0.00              null comment '起驳费金额',
    qbfsfkp        varchar(255)                             null,
    qbfkpcbje      decimal(18, 2) default 0.00              null comment '起驳费开票成本金额',
    create_by      varchar(255)                             null,
    create_time    datetime       default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                             null,
    update_time    datetime       default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                             null,
    data_key       varchar(255)                             null,
    authorized_key varchar(255)                             null,
    fhzt           varchar(255)                             null
)
    comment '发货地定价信息';

create table whdserp_pro.ERP_GYSXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    gysmc          varchar(255)                       null,
    gyslx          varchar(255)                       null,
    hplx           varchar(255)                       null,
    fylx           varchar(255)                       null,
    gs             varchar(255)                       null,
    dwmc           varchar(255)                       null,
    sh             varchar(255)                       null,
    xm             varchar(255)                       null,
    dh             varchar(255)                       null,
    zw             varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '供应商信息';

create index ERP_GYSXX_create_by_index
    on whdserp_pro.ERP_GYSXX (create_by);

create index ERP_GYSXX_create_time_index
    on whdserp_pro.ERP_GYSXX (create_time);

create index ERP_GYSXX_dh_index
    on whdserp_pro.ERP_GYSXX (dh);

create index ERP_GYSXX_dwmc_index
    on whdserp_pro.ERP_GYSXX (dwmc);

create index ERP_GYSXX_fylx_index
    on whdserp_pro.ERP_GYSXX (fylx);

create index ERP_GYSXX_gs_index
    on whdserp_pro.ERP_GYSXX (gs);

create index ERP_GYSXX_gyslx_index
    on whdserp_pro.ERP_GYSXX (gyslx);

create index ERP_GYSXX_gysmc_index
    on whdserp_pro.ERP_GYSXX (gysmc);

create index ERP_GYSXX_hplx_index
    on whdserp_pro.ERP_GYSXX (hplx);

create index ERP_GYSXX_remark_index
    on whdserp_pro.ERP_GYSXX (remark);

create index ERP_GYSXX_sh_index
    on whdserp_pro.ERP_GYSXX (sh);

create index ERP_GYSXX_update_by_index
    on whdserp_pro.ERP_GYSXX (update_by);

create index ERP_GYSXX_update_time_index
    on whdserp_pro.ERP_GYSXX (update_time);

create index ERP_GYSXX_xm_index
    on whdserp_pro.ERP_GYSXX (xm);

create index ERP_GYSXX_zw_index
    on whdserp_pro.ERP_GYSXX (zw);


create table whdserp_pro.ERP_HPXX
(
    cd_id          bigint                             null comment '产地',
    id             bigint auto_increment comment 'ID'
        primary key,
    hplx           varchar(255)                       null,
    gg             varchar(255)                       null,
    pp             varchar(255)                       null,
    lyzczdj        decimal(18, 2)                     null comment '陆运装车指导价',
    cyzczdj        decimal(18, 2)                     null comment '船运装车指导价',
    cycgje         decimal(18, 2)                     null comment '船运采购价',
    lycgje         decimal(18, 2)                     null comment '陆运采购价',
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '货品信息';

create table whdserp_pro.ERP_KHXD
(
    id                 bigint auto_increment comment 'ID'
        primary key,
    khxx_id            bigint                             null,
    zd_id              bigint                             null comment '站点Id',
    hplx               varchar(255)                       null,
    cpgg               varchar(255)                       null,
    cppp               varchar(255)                       null,
    fhdw               decimal(18, 2)                     null comment '发货吨位',
    hyfs               varchar(255)                       null,
    ywlx_code          varchar(255)                       null,
    fhdlx              varchar(255)                       null,
    fhd_id             bigint                             null comment '发货地Id',
    ddze               decimal(18, 2)                     null comment '订单总额',
    dddj               decimal(18, 2)                     null comment '订单单价',
    ddye               decimal(18, 2)                     null comment '订单余额',
    dzsj               datetime default CURRENT_TIMESTAMP null comment '到站时间',
    zjbg               varchar(255)                       null,
    ghfs               varchar(255)                       null,
    ysh                varchar(255)                       null,
    ztclxx             longtext                           null,
    yd                 varchar(255)                       null,
    finished           varchar(255)                       null,
    dd_finished        varchar(255)                       null,
    zjbgyq             varchar(255)                       null,
    sjfhdw             decimal(18, 2)                     null comment '实际发货吨位',
    sjfhze             decimal(18, 2)                     null comment '实际发货总额',
    sjfhdj             decimal(18, 2)                     null comment '实际发货单价',
    create_by          varchar(255)                       null,
    create_time        datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by          varchar(255)                       null,
    update_time        datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark             varchar(255)                       null,
    data_key           longtext                           null,
    authorized_key     varchar(255)                       null,
    ddap_finished_time datetime                           null comment '调度完成时间',
    finished_time      datetime                           null comment '完成时间',
    update_time_xs     datetime                           null,
    ddap_color         varchar(1024)                      null,
    khxd_color         varchar(1024)                      null
)
    comment '客户下单';

create index ERP_KHXD_cpgg_index
    on whdserp_pro.ERP_KHXD (cpgg);

create index ERP_KHXD_cppp_index
    on whdserp_pro.ERP_KHXD (cppp);

create index ERP_KHXD_create_by_index
    on whdserp_pro.ERP_KHXD (create_by);

create index ERP_KHXD_create_time_index
    on whdserp_pro.ERP_KHXD (create_time);

create index ERP_KHXD_dzsj_index
    on whdserp_pro.ERP_KHXD (dzsj);

create index ERP_KHXD_fhd_id_index
    on whdserp_pro.ERP_KHXD (fhd_id);

create index ERP_KHXD_fhdlx_index
    on whdserp_pro.ERP_KHXD (fhdlx);

create index ERP_KHXD_hplx_index
    on whdserp_pro.ERP_KHXD (hplx);

create index ERP_KHXD_khxx_id_index
    on whdserp_pro.ERP_KHXD (khxx_id);

create index ERP_KHXD_update_time_index
    on whdserp_pro.ERP_KHXD (update_time);

create index ERP_KHXD_update_time_xs_index
    on whdserp_pro.ERP_KHXD (update_time_xs);

create index ERP_KHXD_ywlx_code_index
    on whdserp_pro.ERP_KHXD (ywlx_code);

create index ERP_KHXD_zd_id_index
    on whdserp_pro.ERP_KHXD (zd_id);

create table whdserp_pro.ERP_KHXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    khmc           varchar(255)                       null,
    khqc           varchar(255)                       null,
    khlx           varchar(255)                       null,
    user_name      varchar(255)                       null,
    dept_id        bigint                             null comment '部门',
    is_valid       varchar(255)                       null,
    is_in_business varchar(255)                       null,
    htwz           varchar(255)                       null,
    xm             varchar(255)                       null,
    dh             varchar(255)                       null,
    zw             varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null,
    htwz_kf        varchar(255)                       null,
    sn_my_ht       varchar(255)                       null,
    sn_qb_ht       varchar(255)                       null,
    sn_ys_ht       varchar(255)                       null,
    kf_my_ht       varchar(255)                       null,
    kf_qb_ht       varchar(255)                       null,
    kf_ys_ht       varchar(255)                       null,
    constraint ERP_KHXX_khmc_uindex
        unique (khmc)
)
    comment '客户信息';

create index ERP_KHXX_create_by_index
    on whdserp_pro.ERP_KHXX (create_by);

create index ERP_KHXX_create_time_index
    on whdserp_pro.ERP_KHXX (create_time);

create index ERP_KHXX_dept_id_index
    on whdserp_pro.ERP_KHXX (dept_id);

create index ERP_KHXX_htwz_index
    on whdserp_pro.ERP_KHXX (htwz);

create index ERP_KHXX_htwz_kf_index
    on whdserp_pro.ERP_KHXX (htwz_kf);

create index ERP_KHXX_kf_my_ht_index
    on whdserp_pro.ERP_KHXX (kf_my_ht);

create index ERP_KHXX_kf_qb_ht_index
    on whdserp_pro.ERP_KHXX (kf_qb_ht);

create index ERP_KHXX_kf_ys_ht_index
    on whdserp_pro.ERP_KHXX (kf_ys_ht);

create index ERP_KHXX_khlx_index
    on whdserp_pro.ERP_KHXX (khlx);

create index ERP_KHXX_khqc_index
    on whdserp_pro.ERP_KHXX (khqc);

create index ERP_KHXX_sn_my_ht_index
    on whdserp_pro.ERP_KHXX (sn_my_ht);

create index ERP_KHXX_sn_qb_ht_index
    on whdserp_pro.ERP_KHXX (sn_qb_ht);

create index ERP_KHXX_sn_ys_ht_index
    on whdserp_pro.ERP_KHXX (sn_ys_ht);

create index ERP_KHXX_user_name_index
    on whdserp_pro.ERP_KHXX (user_name);

create table whdserp_pro.ERP_MTXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    mc             varchar(255)                       null,
    fhdlx          varchar(255)                       null,
    dzxx           varchar(255)                       null,
    fhd            varchar(255)                       null,
    zy             varchar(255)                       null,
    xm             varchar(255)                       null,
    dh             varchar(255)                       null,
    zw             varchar(255)                       null,
    djfz           varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '码头信息';

create index ERP_MTXX_djfz_index
    on whdserp_pro.ERP_MTXX (djfz);

create index ERP_MTXX_fhd_index
    on whdserp_pro.ERP_MTXX (fhd);

create index ERP_MTXX_fhdlx_index
    on whdserp_pro.ERP_MTXX (fhdlx);

create index ERP_MTXX_mc_index
    on whdserp_pro.ERP_MTXX (mc);

create index ERP_MTXX_zy_index
    on whdserp_pro.ERP_MTXX (zy);

create table whdserp_pro.ERP_PPXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    hplx           varchar(255)                       null,
    pp             varchar(255)                       null,
    px             bigint   default 1                 null comment '排序',
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '品牌信息';

create index ERP_PPXX_hplx_index
    on whdserp_pro.ERP_PPXX (hplx);

create index ERP_PPXX_pp_index
    on whdserp_pro.ERP_PPXX (pp);

create index ERP_PPXX_px_index
    on whdserp_pro.ERP_PPXX (px);


create table whdserp_pro.ERP_ZDXX
(
    id             bigint auto_increment comment 'ID'
        primary key,
    khxx_id        bigint                             null comment '客户',
    zdmc           varchar(255)                       null,
    dzxx           varchar(255)                       null,
    hplx           varchar(255)                       null,
    zdlx           varchar(255)                       null,
    xszt           varchar(255)                       null,
    gdkcwc         varchar(255)                       null,
    cjr            varchar(255)                       null,
    cjrq           datetime                           null comment '创建日期',
    zdzp           longtext                           null,
    kczp           longtext                           null,
    zdtx           varchar(255)                       null,
    xm             varchar(255)                       null,
    dh             varchar(255)                       null,
    zw             varchar(255)                       null,
    create_by      varchar(255)                       null,
    create_time    datetime default CURRENT_TIMESTAMP null comment '创建时间',
    update_by      varchar(255)                       null,
    update_time    datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment '更新时间',
    remark         varchar(255)                       null,
    data_key       varchar(255)                       null,
    authorized_key varchar(255)                       null
)
    comment '站点信息';

create index ERP_ZDXX_cjr_index
    on whdserp_pro.ERP_ZDXX (cjr);

create index ERP_ZDXX_cjrq_index
    on whdserp_pro.ERP_ZDXX (cjrq);

create index ERP_ZDXX_create_time_index
    on whdserp_pro.ERP_ZDXX (create_time);

create index ERP_ZDXX_hplx_index
    on whdserp_pro.ERP_ZDXX (hplx);

create index ERP_ZDXX_khxx_id_index
    on whdserp_pro.ERP_ZDXX (khxx_id);

create index ERP_ZDXX_update_time_index
    on whdserp_pro.ERP_ZDXX (update_time);

create index ERP_ZDXX_xszt_index
    on whdserp_pro.ERP_ZDXX (xszt);

create index ERP_ZDXX_zdlx_index
    on whdserp_pro.ERP_ZDXX (zdlx);






