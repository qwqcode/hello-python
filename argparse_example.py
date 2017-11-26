import argparse
import textwrap

VERSION = '1.0'


def parse_args():
    parser = argparse.ArgumentParser(
        description='一个关于 XXX 的工具',
        usage='%(prog)s [选项] BOARD [BOARD..]',  # %(prog)s 当前文件名
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            在使用 XXX 之前，请访问
            example://example/xxx
            生成访问令牌。打开 “read_public” 权限。

            XXX 将在以下情况使用您的访问令牌
            （按优先次序）：
              * -a, --access-token 参数
              * 当前工作目录下的 access_token 文件
              * access_token 文件与 %(prog)s 所在的目录相同

            在 Windows 上，不要忘记在命令提示符下启用 UTF-8
            如果你的 Python 版本 < 3.6.0：
              chcp 65001
            或者改为设置 PYTHONIOENCODING 环境变量：
              set PYTHONIOENCODING=UTF-8
            """))

    """
    方法 add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
    name 或 flags：命令行参数名或者选项，如上面的address或者-p,--port.其中命令行参数如果没给定，且没有设置 defualt，则出错。但是如果是选项的话，则设置为 None
    nargs：命令行参数的个数，一般使用通配符表示，其中，'?'表示只用一个，'*'表示0到多个，'+'表示至少一个
    default：默认值
    type：参数的类型，默认是字符串string类型，还有float、int等类型
    help：和ArgumentParser方法中的参数作用相似，出现的场合也一致
    """
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)

    parser.add_argument(
        'boards', nargs='*',
        help=(
            '下载 List 或 boards. 每个 item 可以为完整的 board URL,'
            'user_name/board_name 组合 或 board id.'
            '也可以是 "all" 下载你所有公开的 boards.'
        )
    )

    parser.add_argument(
        '-b', '--batch-file', metavar='文件',
        type=argparse.FileType('r', encoding='utf-8'),
        help='File containing boards to download (or "-" for stdin).'
    )

    parser.add_argument(
        '-a', '--access-token', metavar='令牌',
        help='使用访问令牌来代替保存在文件中的.'
    )

    parser.add_argument(
        '-o', '--out-dir', metavar='目录', default='.',
        help=(
            '保存图像的目录.'
            '默认值是当前工作目录.'
        )
    )

    parser.add_argument(
        '-t', '--threads', type=int, default=10,
        help='下载线程数. 默认值是 10.'
    )

    parser.add_argument(
        '-d', '--debug', action='store_const',
        dest='loglevel', const='D',
        help='打印调试信息.'
    )

    args = parser.parse_args()
    if not args.batch_file and not args.boards:
        parser.error('您必须提供至少一个 board.')

    if args.threads < 1:
        parser.error('线程的数量必须 >= 1')

    return args


app_args = parse_args()
print(app_args)
