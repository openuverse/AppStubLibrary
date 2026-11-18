# AppStubLibrary

用于收集多个应用接口文件的中央仓库。每个应用在 `stubs/{app_id}/` 下按版本存放接口文件，并在 `manifest.json` 里声明版本和安装路径。

## 功能概览

| 功能 | 说明 |
|-----|------|
| 多仓库接口文件管理 | 集中存储多个应用的接口文件 |
| 版本管理 | 按版本目录组织，并标记 `latest` |
| 路径映射 | 每个版本可以把文件夹映射到目标工程中的安装路径 |
| 目录隔离 | 每个应用只维护自己的目录 |
| 版本不可变 | 已发布版本的内容不能再改 |

## 目录结构

```
AppStubLibrary/
├── index.json              # 全局索引
├── index.schema.json       # 索引格式
├── stubs/                  # 接口文件
│   └── {app_id}/
│       ├── manifest.json   # 应用元信息
│       └── tags/
│           └── {version}/  # 版本目录
│               ├── frontend/
│               │   ├── actions.ts
│               │   └── attributes.ts
│               └── backend/
│                   ├── __init__.py
│                   └── action.py
└── README.md
```

## manifest.json 格式

```json
{
  "id": "your-app-id",
  "name": "应用显示名称",
  "description": "可选描述",
  "latest": "0.0.1",
  "tags": [
    {
      "version": "0.0.1",
      "mappings": {
        "frontend": "src/stub",
        "backend": "stub"
      }
    }
  ],
  "maintainers": [
    { "type": "user", "name": "your-name" }
  ]
}
```

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|-----|------|-----|------|
| `id` | string | 是 | 应用唯一标识，必须与目录名一致 |
| `name` | string | 是 | 显示名称 |
| `latest` | string | 是 | 最新版本号，必须出现在 `tags` 中 |
| `tags` | array | 是 | 版本列表，每个元素包含 `version` 和 `mappings` |
| `maintainers` | array | 是 | 维护者列表，只支持用户 |
| `description` | string | 否 | 描述 |

### tags 格式

| 字段 | 类型 | 必填 | 说明 |
|-----|------|-----|------|
| `version` | string | 是 | 版本号，对应 `tags/{version}/` 目录 |
| `mappings` | object | 是 | 路径映射。key 是版本目录下的文件夹名，value 是安装到目标工程中的相对路径 |

示例：

```json
{
  "version": "0.0.1",
  "mappings": {
    "frontend": "src/stub",
    "backend": "stub"
  }
}
```

这表示：

- `tags/0.0.1/frontend/` 会安装到目标工程前端的 `src/stub/`
- `tags/0.0.1/backend/` 会安装到目标工程后端的 `stub/`

### maintainers 格式

```json
{
  "maintainers": [
    { "type": "user", "name": "your-name" }
  ]
}
```

- `type` 必须为 `user`
- `name` 是维护者名称

## 版本目录要求

每个 `tags/{version}/` 需要满足：

1. 文件放在子文件夹里，不要直接放在版本目录下
2. 子文件夹与 `mappings` 的 key 一一对应
3. 每个子文件夹里都要有文件
4. 不要使用符号链接

```
tags/0.0.1/
├── frontend/
│   ├── actions.ts
│   └── attributes.ts
└── backend/
    ├── __init__.py
    └── action.py
```

## 如何提交一个应用

```
stubs/your-app-id/
├── manifest.json
└── tags/
    └── 0.0.1/
        ├── frontend/
        │   └── actions.ts
        └── backend/
            └── action.py
```

在 `manifest.json` 的 `maintainers` 里写上维护者。已发布版本不能修改、删除或重命名；需要修正时请新增一个版本，例如 `0.0.2`。

## index.json

`index.json` 由仓库维护流程生成，汇总每个应用的 `id`、`name`、`latest`、`tags` 和 `maintainers`。格式见 `index.schema.json`。

## 常见问题

### 如何更新已发布的版本？

已发布版本的内容不能改。请新增一个版本，例如 `0.0.2`，并把 `latest` 指到它。

### mappings 是什么？

它声明版本目录中的文件夹要安装到目标工程的哪个相对路径。例如 `"frontend": "src/stub"` 表示 `tags/{version}/frontend/` 安装到前端工程的 `src/stub/`。

### 为什么不能往已发布版本里加文件？

版本一旦发布，目录内容就固定了。不能新增、修改、删除或重命名其中的文件。请创建新版本。
