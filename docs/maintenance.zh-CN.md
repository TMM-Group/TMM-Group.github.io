# 课题组网站维护说明

网站地址：https://tmm-group.github.io/

这个网站采用“内容文件 → 生成网页 → 提交到 GitHub”的方式。修改内容后，需要运行一次 `python scripts/build.py`，再把内容文件和生成后的网页一起提交。GitHub Pages 会自动发布 `main` 分支中的网页。

**目前仅在 GitHub 网页上修改 `data/*.json`，不会自动重新生成网站。** 建议在电脑上的仓库中修改，然后生成并上传。不要把生成的 `index.html` 当作长期维护入口：下一次生成会覆盖手工修改。

## 每个页面改哪里

| 页面或内容 | 修改文件 | 具体位置 |
| --- | --- | --- |
| Research 研究内容 | `data/research.json` | 每个方向的 `title`、`summary`、`paragraphs`、`references`、`image` |
| People 学生和校友 | `data/people.json` | `groups` 下各组的 `people` 列表 |
| People 的 Gang Tang 简介 | `scripts/build.py` | 搜索 `def team_page()` |
| Publications 论文 | `data/publications.json` | 已发表/已接收放在 `published`，投稿中/准备中放在 `manuscripts` |
| Software 软件与数据库 | `data/software.json` | `name`、`summary`、`description`、`links`、`image` |
| Join Us 招生内容 | `scripts/build.py` | 搜索 `def join_page()` |
| 首页介绍、按钮和栏目文案 | `scripts/build.py` | 搜索 `def home()` |
| 首页精选论文 | `scripts/build.py` | `home()` 中的 `for number,image in ...`，数字对应论文 `id` |
| 首页钙钛矿示意图 | `assets/perovskite.png` | 当前为青绿配色、深蓝背景图片；换文件名时同步修改 `scripts/build.py` 中的图片路径并重新生成网页 |
| 导航栏、页脚、邮箱等 | `scripts/build.py` | `navigation()`、`footer()`；邮箱全文搜索 `gtang@bit.edu.cn` |
| 字号、颜色、间距、头像尺寸 | `assets/site.css` | 修改相应样式；日常更新内容通常不用改 |

首页的研究、软件和学生简介会读取同一批 `data` 内容。首页成员目前显示 Gang Tang 和在读成员列表的前五位；全部成员仍在 People 页面显示。

## 更新或增加成员

在 `data/people.json` 中找到相应人员，修改 `name`、`description` 或 `image`。新增人员时，复制同组中的一条记录，修改内容，例如：

```json
{
  "id": "new-member",
  "name": "New Member",
  "image": "team/new-member.jpg",
  "description": "Ferroelectricity, Machine learning potentials"
}
```

把新照片放在 `team/` 文件夹，`image` 填写对应的相对路径。文件名建议使用小写英文和连字符；文件名大小写必须一致。照片在页面中采用 4:5 竖幅、顶部对齐，选图时给头顶留一点空白。

成员毕业时，把整条记录从在读组移动到 Alumni 组，再更新去向。保留已有的 `id`，可以避免过去的成员链接失效。

Gang Tang 的当前照片是 `team/tg-white.png`，其首页和 People 页面引用位于 `scripts/build.py`。Yutong Li、Tao Hu 的当前照片分别是 `team/liyutong-white.png` 和 `team/hutao-white.png`。原照片仍保留。

Caidong Shuang 的现有照片两侧留白较多，页面对这张照片作了轻微放大裁切，样式在 `assets/site.css` 的 `#Caidong-Shuang` 规则中。以后更换为取景更紧的照片时，可删除该条专用规则。

## 更新论文

在 `data/publications.json` 的 `published` 列表中复制最上面一条记录，再填写新论文。最新论文放在前面；同一年份集中排列。

- `id`：唯一的数字编号，新论文使用比现有最大编号更大的数字。
- `year`：年份字符串，例如 `"2026"`。
- `title`、`authors`、`citation`：论文标题、作者、期刊信息。
- `link`：论文 DOI 或出版社地址；还没有链接时填写 `""`。
- `status`：已发表用 `"published"`，已接收用 `"accepted"`。
- `notes`：共同贡献等备注，无备注用 `""`。
- `topics`：仅供页面顶部主题筛选使用，不会显示在论文下方。可沿用已有主题；不需要分类时用 `[]`。

化学下标可写成 `N<sub>3</sub>`，作者强调可写成 `<strong>Gang Tang</strong>`。论文总数和年份导航会自动更新。

投稿中论文见 `manuscripts`，沿用现有记录的 `status` 和 `html` 字段。论文正式接收后，在 `published` 中增加完整记录，并从 `manuscripts` 移除对应条目。

JSON 中字符串要使用英文双引号，记录之间要有逗号，列表最后一项后面不要加逗号。正文中如需英文双引号，写成 `\"`。

## 在这台电脑上更新和预览

本地仓库：`H:\AI Agent\chatgpt\tmm-group-website`。需要 Python 3.10 或更新版本，以及 Git。已安装的环境可以直接使用。

1. 打开 PowerShell，进入仓库。先检查有没有尚未提交的修改，再切到 main 并同步：

   ```powershell
   Set-Location 'H:\AI Agent\chatgpt\tmm-group-website'
   git status
   git switch main
   git pull --ff-only origin main
   ```

   如果 `git status` 显示有之前未提交的修改，先保存并提交这些修改，或继续在原分支完成它们，不要直接覆盖。

2. 用编辑器修改对应内容或图片，然后生成网页并检查站内链接：

   ```powershell
   python scripts/build.py
   python -m unittest discover -s tests -k test_pages_local_links_and_assets
   ```

   仓库中的旧资料一致性测试用于最初的改版验收，固定比较当时的 50 篇论文和 5 篇稿件。以后新增或修订论文时，该项测试也需要维护；上面的日常链接检查不依赖固定论文数量。

3. 启动本地预览：

   ```powershell
   python -m http.server 4173 --bind 127.0.0.1
   ```

   浏览器打开 http://127.0.0.1:4173/ ，检查刚改的页面。关闭预览服务时，在 PowerShell 中按 `Ctrl+C`。

4. 确认效果后提交。`git add .` 会加入该仓库内的全部非忽略修改，所以先用 `git status` 和 `git diff` 确认文件列表：

   ```powershell
   git status
   git diff
   git add .
   git commit -m "Update group website content"
   git push origin main
   ```

5. 在 GitHub 仓库的 **Actions** 中查看 `pages build and deployment`。成功后刷新正式网站；如果仍看到旧内容，可按 `Ctrl+F5`。

## 保留旧版和恢复

网站改版前的 main 已备份在 `codex/backup-main-before-redesign-2026-11-15` 分支。平时不用修改这个备份分支。

要撤销最近一次更新，可以对对应提交使用 `git revert`，或请协作者按提交记录恢复。恢复整个改版前的网站时，以备份分支的内容为依据进行恢复，再发布到 main。
