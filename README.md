# appstublibrary

用于收集和管理多个源仓库接口文件的中央仓库。

> **公开仓库**：所有用户都可以通过 MR 方式提交代码。

## 功能概览

| 功能 | 说明 |
|-----|------|
| 📦 **多仓库接口文件管理** | 集中存储多个源仓库的接口文件 |
| 🏷️ **版本管理** | 支持按版本 tag 组织，支持 `latest` 标记 |
| 📁 **路径映射** | 每个版本支持配置文件夹到目标路径的映射 |
| 🔐 **权限隔离** | 每个仓库只能修改自己的目录 |
| 🔒 **版本不可变** | 已发布版本内容不可修改 |
| 👥 **用户/群组权限** | 支持 GitLab 用户和群组权限控制 |
| 🤖 **CI 自动化** | 自动生成索引和权限配置 |
| 🌐 **公开访问** | 公开仓库，所有用户可提交 MR |

---

## 权限规则

| 用户类型 | push | MR | 可修改范围 |
|---------|------|-----|-----------|
| **管理员** @sn06473 @sn06009 @sn04646 @sn03185 | ✅ | ✅ | 所有文件 |
| **CI Bot** @project_338_bot | ✅ | ❌ | 仅 index.json |
| **所有用户** | ❌ | ✅ | 仅自己的 `stubs/{app_id}/` |

> **公开仓库**：任何 GitLab 用户都可以通过 MR 提交代码，只需在 `manifest.json` 的 `maintainers` 中添加自己即可获得对应目录的修改权限。

> **版本保护**：已发布版本 (`stubs/{id}/tags/{version}/`) 内容不可修改、删除或重命名，如需修复请发布新版本。

---

## 目录结构

```
appstublibrary/
├── index.json              # 全局索引文件（CI 自动生成）
├── index.schema.json       # 索引文件格式定义
├── .gitlab-ci.yml          # CI/CD 配置
├── .gitmodules             # 子模块配置
├── stubs/                  # 接口文件目录（所有成员可见）
│   └── {app_id}/
│       ├── manifest.json   # 仓库元信息
│       └── tags/
│           └── {version}/  # 版本目录
│               ├── frontend/       # 映射文件夹
│               │   ├── actions.ts
│               │   └── attributes.ts
│               └── backend/        # 映射文件夹
│                   ├── __init__.py
│                   └── action.py
├── admin/                  # 管理子模块（私有，仅管理员可见）
│   ├── .gitlab-ci.yml
│   ├── CODEOWNERS
│   ├── README.md
│   └── scripts/
│       ├── main/
│       │   ├── validate-ownership.py
│       │   ├── validate-manifest.py
│       │   ├── validate-files.py
│       │   ├── generate-index.py
│       │   ├── generate-codeowners.py
│       │   └── commit-changes.py
│       └── local/
│           └── validate-codeowners.py
└── README.md               # 本文件
```

---

## 文件可见性

| 文件/目录 | 所有成员 | 仅管理员 |
|----------|---------|---------|
| `index.json` | ✅ 可见 | ✅ |
| `stubs/` | ✅ 可见 | ✅ |
| `admin/`（子模块） | ❌ 不可见 | ✅ 可见 |

> 注意：`admin/` 是一个私有 Git 子模块，非管理员 clone 时不会获取该目录内容。

---

## manifest.json 格式

```json
{
  "id": "your-app-id",
  "name": "仓库显示名称",
  "description": "可选描述",
  "latest": "0.0.1",
  "tags": [
    {
      "version": "0.0.1",
      "mappings": {
        "frontend": "frontend/src/stub",
        "backend": "backend/stub"
      }
    }
  ],
  "maintainers": [
    { "type": "user", "name": "zhangsan" },
    { "type": "group", "name": "UltraVIEW" }
  ]
}
```

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|-----|------|-----|------|
| `id` | string | ✅ | 仓库唯一标识，必须与目录名一致 |
| `name` | string | ✅ | 显示名称（可重复） |
| `latest` | string | ✅ | 最新版本号，必须在 tags 中 |
| `tags` | array | ✅ | 版本列表，每个元素包含 version 和 mappings |
| `maintainers` | array | ✅ | 维护者列表（用户/群组） |
| `description` | string | | 描述（可选） |

### tags 格式

每个 tag 是一个对象，包含：

| 字段 | 类型 | 必填 | 说明 |
|-----|------|-----|------|
| `version` | string | ✅ | 版本号，对应 `tags/{version}/` 目录 |
| `mappings` | object | ✅ | 路径映射，key 是目录名，value 是目标安装路径 |

**mappings 说明**：
- key：`tags/{version}/` 下的文件夹名（如 `frontend`、`backend`）
- value：目标项目中的安装路径（如 `frontend/src/stub`）

**示例**：
```json
{
  "version": "0.0.1",
  "mappings": {
    "frontend": "frontend/src/stub",
    "backend": "backend/stub"
  }
}
```
上述配置表示：
- `tags/0.0.1/frontend/` 的内容会被安装到目标项目的 `frontend/src/stub/`
- `tags/0.0.1/backend/` 的内容会被安装到目标项目的 `backend/stub/`

### maintainers 格式

```json
{
  "maintainers": [
    { "type": "user", "name": "zhangsan" },
    { "type": "group", "name": "UltraVIEW" },
    { "type": "group", "name": "UltraVIEW/Backend" }
  ]
}
```

- `type`: `user`（用户）或 `group`（群组）
- `name`: GitLab 用户名或群组路径（从 URL 获取）

---

## 版本目录结构要求

每个版本目录 (`tags/{version}/`) 必须满足：

1. **不能直接放文件**：所有文件必须放在子文件夹中
2. **子文件夹与 mappings 一一对应**：mappings 的 key 必须与实际目录名匹配
3. **每个子文件夹必须有文件**：不允许空文件夹
4. **不允许符号链接**

正确示例：
```
tags/0.0.1/
├── frontend/           # 对应 mappings["frontend"]
│   ├── actions.ts
│   └── attributes.ts
└── backend/            # 对应 mappings["backend"]
    ├── __init__.py
    └── action.py
```

错误示例：
```
tags/0.0.1/
├── actions.ts          # ❌ 不能直接放文件
└── frontend/
```

---

## 接入流程

> **公开仓库**：任何 GitLab 用户都可以通过以下流程接入。

### 新建仓库

1. **Fork 本仓库或创建分支**

2. **创建仓库目录和 manifest.json**

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

3. **提交 MR**

```bash
git add stubs/your-app-id/
git commit -m "feat: add your-app-id v0.0.1"
git push origin your-branch
# 在 GitLab 上创建 MR
```

4. **等待 CI 验证**
   - 验证权限（validate-ownership）
   - 验证 manifest 格式（validate-manifest）
   - 验证目录结构（validate-files）

5. **合并后 CI 自动处理**
   - 自动生成 index.json
   - 自动生成 CODEOWNERS

---

## CI/CD 流程

### 验证阶段（push 和 MR 都执行）

| 任务 | 说明 | 失败阻塞 |
|-----|------|---------|
| `validate-ownership` | 验证提交者权限、版本不可变性 | ✅ |
| `validate-manifest` | 验证 manifest.json 格式和必填字段 | ✅ |
| `validate-files` | 验证目录结构和安全检查 | ✅ |

### 部署阶段（合并后，stubs/ 有变化时执行）

| 任务 | 说明 |
|-----|------|
| `generate-configs` | 自动生成 index.json 和 CODEOWNERS |

---

## index.json 格式（CI 自动生成）

```json
{
  "$schema": "./index.schema.json",
  "version": "1.0.0",
  "updated_at": "2026-01-15T00:00:00Z",
  "repos": [
    {
      "id": "app-a",
      "name": "仓库A",
      "description": "描述",
      "latest": "0.0.2",
      "tags": [
        {
          "version": "0.0.1",
          "mappings": {
            "frontend": "frontend/src/stub",
            "backend": "backend/stub"
          }
        },
        {
          "version": "0.0.2",
          "mappings": {
            "frontend": "frontend/src/stub",
            "backend": "backend/stub"
          }
        }
      ],
      "maintainers": [
        { "type": "user", "name": "zhangsan" }
      ]
    }
  ]
}
```

---

## GitLab 配置要求

### 主仓库（appstublibrary）

**分支保护** (Settings → Repository → Protected branches)

| 设置 | 值 |
|-----|-----|
| Branch | `master` |
| Allowed to merge | `Developers + Maintainers` |
| Allowed to push | `Maintainers` |

**CI/CD 变量** (Settings → CI/CD → Variables)

| 变量 | 用途 |
|-----|------|
| `DEPLOY_TOKEN` | 克隆 admin 子模块 |
| `STUB_WRITE_TOKEN` | 推送 index.json |
| `PROJECT_WRITE_TOKEN` | 推送 CODEOWNERS |

### 私有子模块（appstubadmin）

| 设置 | 值 |
|-----|-----|
| Visibility | Private |
| Members | @sn06473, @sn06009, @sn04646, @sn03185 |

---

## 常见问题

### Q: 新仓库首次提交时如何获得权限？

CI 会从提交中的 `manifest.json` 读取 `maintainers` 进行权限验证，无需预先配置。

### Q: 群组名怎么获取？

从 GitLab URL 获取，如 `http://bjrdgit.rigoltech.com/UltraVIEW`，群组名是 `UltraVIEW`。

### Q: 为什么看不到 admin 目录？

`admin/` 是私有子模块，仅管理员可见。普通成员 clone 时不会获取该目录。

### Q: 如何更新已发布的版本？

**已发布版本内容不可修改**。如需修复，请发布新版本（如 `0.0.2`）。

### Q: mappings 是什么意思？

mappings 定义了文件夹到目标路径的映射关系。例如：
- `"frontend": "frontend/src/stub"` 表示 `tags/{version}/frontend/` 的内容会被安装到目标项目的 `frontend/src/stub/` 目录

### Q: 为什么 CI 报错 "不能往已发布版本新增文件"？

版本一旦发布，其目录内容不可变。不能新增、修改、删除或重命名文件。请创建新版本。

### Q: 任何人都可以提交吗？

是的，这是公开仓库。任何 GitLab 用户都可以通过 MR 方式提交。在 `manifest.json` 的 `maintainers` 中添加自己即可获得对应目录的修改权限。

---

## 联系方式

如有问题，请联系管理员 @sn06473 @sn06009 @sn04646 @sn03185 或提交 Issue。
