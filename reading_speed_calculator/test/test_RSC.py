from ..lib.rsc import *
def test_rsc():
    build = rsc("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec justo elit, mollis quis nunc nec, rutrum sollicitudin eros. Donec urna mi, tempus vel ipsum et, consectetur sagittis leo. Duis euismod arcu sit amet dignissim pretium. Ut arcu urna, tempor quis rhoncus a, tempus in nibh. Nulla ac viverra nisl. Proin semper faucibus sapien, quis tempor turpis tempor nec. Ut mi purus, mattis quis lorem vel, maximus consequat felis. Curabitur feugiat lacus eu nisi lobortis, eget pharetra dui euismod. Nam at erat quam. Donec vestibulum justo scelerisque sem maximus dictum. Sed sagittis nisl nec vestibulum blandit. Etiam eu accumsan nisi. Ut laoreet varius fermentum. Phasellus convallis augue vitae libero tincidunt, quis vestibulum mi dapibus. Integer ipsum urna, aliquam pharetra justo a, suscipit venenatis ligula. Suspendisse ut hendrerit mauris, quis congue erat. In pulvinar nibh at efficitur faucibus. Nullam dolor metus, dapibus non nibh at, fermentum molestie erat. Proin aliquam aliquet lectus vel mattis. Sed auctor arcu vel libero egestas pulvinar. Etiam lectus est, hendrerit id rutrum eu, cursus sed elit. Phasellus vestibulum mauris dolor, sit amet congue tellus facilisis eget. Nullam vulputate aliquet risus, gravida tempus enim fermentum non. Praesent porta felis quis varius dapibus. Etiam porttitor interdum quam, quis ultricies.")
    assert build == 1
    build = rsc(7)
    assert build == "enter a valid string"